import pytest

from pathlib import Path
from otoe.exceptions import , OtoeEmptyDirectoryError, OtoeFileNotFoundError, OtoeMarkdownFileNotFoundError, OtoeNoMatchesError
from otoe.obsidian import ObsidianParser


class TestObsidianParser:

    def test_md_dir_not_found(self):
        with pytest.raises(OtoeFileNotFoundError):
            ObsidianParser('not_found')

    def test_md_dir_empty(self, data_path: Path):
        dir_path = data_path / 'empty_dir'
        with pytest.raises(OtoeMarkdownFileNotFoundError):
            ObsidianParser(dir_path).get_md_files()

    def test_md_dir_only_dirs(self, data_path: Path):
        dir_path = data_path / 'only_dirs'
        with pytest.raises(OtoeMarkdownFileNotFoundError):
            ObsidianParser(dir_path).get_md_files()

    def test_md_dir_only_files(self, data_path: Path):
        dir_path = data_path / 'only_files'
        data = ObsidianParser(dir_path).get_md_files()
        assert 'base' in data
        assert sorted(data['base']) == [dir_path / f for f in ['test.md', 'test2.md']]

    # test if dir contains files and empty directories
    def test_md_dir_files_and_empty_dirs(self, data_path: Path):
        dir_path = data_path / 'files_and_empty_dirs'
        data = ObsidianParser(dir_path).get_md_files()
        assert 'base' in data
        assert len(data) == 1, 'empty directories should not be included in the result'
        assert sorted(data['base']) == [dir_path / f for f in ['test.md', 'test2.md']]
        
    # test only md files are processed
    def test_only_md_files_are_processed(self, data_path: Path):
        dir_path = data_path / 'non_md_files_with_dirs'
        data = ObsidianParser(dir_path).get_md_files()
        assert 'base' in data
        assert 'dir' in data
        assert sorted(data['base']) == [dir_path / f for f in ['test.md']]
        assert sorted(data['dir']) == [dir_path / 'dir' / f for f in ['test.md']]

    # test if dir contains files and directories and files are markdown and yaml is empty
    def test_md_with_no_yaml_are_omitted(self, data_path: Path):
        dir_path = data_path / 'empty_yamls'
        with pytest.raises(OtoeNoMatchesError):
            ObsidianParser(dir_path).generate_matches()
        
    # test if dir contains files and directories and files are markdown and yaml is valid and markdown is empty
    def test_md_with_no_text_are_omitted(self, data_path: Path):
        dir_path = data_path / 'empty_md'
        with pytest.raises(OtoeNoMatchesError):
            ObsidianParser(dir_path).generate_matches()
            
    def test_md_with_yaml_are_processed(self, data_path: Path):
        dir_path = data_path / 'valid'
        data = ObsidianParser(dir_path).generate_matches()
        for dir in ['base', 'dir']:
            assert dir in data
            assert len(data[dir]) == 1
            match = data[dir][0]
            assert match == {'trigger': 'keyword', 'replace': 'test'}

