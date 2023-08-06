import yaml
import argparse
import shutil
from collections import defaultdict
from pathlib import Path
from otoe.config import SEPARATOR, TRIGGER

from otoe.exceptions import OtoeEmptyMarkdownError, OtoeEmptyYamlError, OtoeFileNotFoundError, OtoeMarkdownFileNotFoundError, OtoeNoMatchesError, OtoeValueError


class MarkDownParser:

    def __init__(self, file: str | Path):
        file_path = Path(file)
        if not file_path.exists():
            raise OtoeFileNotFoundError(f"File {file} not found")
        self.file_path = file_path
        self.data: str = self.load()

    def load(self):
        with open(self.file_path, 'r') as f:
            data = f.read()
        return data

    def parse_md_part(self, replace_text: str):
        parsed_text = replace_text.strip()
        if not parsed_text:
            raise OtoeEmptyMarkdownError(f'File {self.file_path} has empty markdown part')
        return parsed_text

    def parse_yaml_part(self, yaml_str: str) -> dict:
        yaml_str = yaml_str.replace(r'/t', ' ' * 4)
        yaml_dict = yaml.load(yaml_str, Loader=yaml.FullLoader)
        if not yaml_dict:
            raise OtoeEmptyYamlError(f'File {self.file_path} has empty yaml part')

        if TRIGGER not in yaml_dict:
            raise OtoeValueError(f'File {self.file_path} has no trigger')
        return yaml_dict
    
    def parse(self):
        splitted_data = self.data.split(SEPARATOR)
        if len(splitted_data) > 2:
            splitted_data = [SEPARATOR.join(splitted_data[:-1]), splitted_data[-1]]
        elif len(splitted_data) < 2:
            raise OtoeValueError(f'File {self.file_path} has no separator')
        replace_text = splitted_data[0]
        yaml_text = splitted_data[1]
        match = self.parse_yaml_part(yaml_text)
        match['replace'] = self.parse_md_part(replace_text)
        return match


class ObsidianParser:
    """
    Parse Obsidian markdown files
    md_dir: directory where the markdown files are located
    md_dir can also contain directories with markdown files
    """

    def __init__(self, md_dir: str | Path, per_project: bool = True):
        md_dir_path = Path(md_dir)
        if not md_dir_path.exists():
            raise OtoeFileNotFoundError(f"Directory {md_dir} not found")
        self.md_dir_path = md_dir_path
        self.fast_fail = True

        self.parser = MarkDownParser
        self.per_project = per_project


    def get_md_files(self) -> dict[str, list[Path]]:
        files_by_dir = defaultdict(list)
        f_count = 0
        for file in self.md_dir_path.iterdir():
            print(file)
            if file.is_dir():
                files = [f for f in file.iterdir() if f.is_file() and f.suffix == '.md']
                if files:
                    f_count += len(files)
                    files_by_dir[file.name] = files
            elif file.suffix == '.md':
                f_count += 1
                files_by_dir['base'].append(file)
        if not f_count:
            raise OtoeMarkdownFileNotFoundError(f"No markdown files found in {self.md_dir_path}")
        return files_by_dir

    def parse_md_file(self, file: Path) -> dict:
        return self.parser(file).parse()

    def generate_matches(self) -> dict:
        matches = defaultdict(list)
        files_by_dir = self.get_md_files()
        for dir_name, files in files_by_dir.items():
            for file in files:
                try:
                    match = self.parse_md_file(file)
                    matches[dir_name].append(match)
                except Exception as e:
                    print(f"Error parsing {file}: {e}")
        if not matches:
            raise OtoeNoMatchesError(f"Cannot construct any match from {self.md_dir_path}")
        return matches

    def write_yamls(self, matches: dict[str, list[dict]]):
        print(self.per_project)
        matches_to_write: dict[str, list[dict]] = (matches if self.per_project else {
            'base': [
                match
                for project_matches in matches.values()
                for match in project_matches
            ]
        })
        print(matches_to_write.keys())
        path = self.md_dir_path / '!espanso'
        try:
            path.mkdir()
        except FileExistsError:
            print(f"Directory {path} already exists. Do you want to override it? [yes/no]")
            confirm = input()
            # 
            if confirm.lower() == 'yes':
                # delete directory even if it is not empty
                shutil.rmtree(path)
                path.mkdir()
            else:
                print("Exiting")
                return
        for file_name, project_matches in matches_to_write.items():
            file_path = path / f"{file_name}.yml"
            with open(file_path, 'w') as f:
                yaml.dump({'matches': project_matches}, f, encoding='utf-8', allow_unicode=True)
            print(f"Written {len(project_matches)} matches to {file_name}.yaml")
            print(f"File {file_path} written")

