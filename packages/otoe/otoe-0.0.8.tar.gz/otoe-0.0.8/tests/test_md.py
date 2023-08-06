import pytest
from pathlib import Path
from otoe.exceptions import OtoeEmptyMarkdownError, OtoeEmptyYamlError, OtoeFileNotFoundError

from otoe.obsidian import MarkDownParser


class TestMD:

    def test_load(self, data_path: Path):
        file_path = data_path / 'test_load.md'
        md = MarkDownParser(file_path)
        assert md.data.strip() == 'test'

    def test_load_not_existing(self, data_path: Path):
        file_path = data_path / 'not_existing.md'
        with pytest.raises(OtoeFileNotFoundError):
            MarkDownParser(file_path)


    def test_parse_md_part(self, data_path: Path):
        file_path = data_path / 'test_parse_md.md'
        md = MarkDownParser(file_path)
        assert md.parse_md_part(md.data) == 'tests\nline2'

    def test_parse_yaml_trigger(self, data_path: Path):
        file_path = data_path / 'test_trigger.md'
        md = MarkDownParser(file_path)
        assert md.parse_yaml_part(md.data) == {'trigger': ':keyword'}
        
    def test_parse_yaml_part(self, data_path: Path):
        file_path = data_path / 'test_parse_yaml.md'
        md = MarkDownParser(file_path)
        assert md.parse_yaml_part(md.data) == {'trigger': ':year', 'vars': [{'format': '%Y', 'name': 'year', 'type': 'date'}]}


    def test_parse_md(self, data_path: Path):
        file_path = data_path / 'test.md'
        md = MarkDownParser(file_path)
        assert md.parse() == {'trigger': ':test', 'replace': 'here is some text'}

    def test_parse_empty_md_part(self, data_path: Path):
        file_path = data_path / 'empty.md'
        with pytest.raises(OtoeEmptyMarkdownError):
            md = MarkDownParser(file_path)
            md.parse_md_part(md.data)

    def test_parse_empty_yaml_part(self, data_path: Path):
        file_path = data_path / 'empty.md'
        with pytest.raises(OtoeEmptyYamlError):
            md = MarkDownParser(file_path)
            md.parse_yaml_part(md.data)

    def test_md_with_separator_in_text(self, data_path: Path):
        file_path = data_path / 'contains_separator.md'
        md = MarkDownParser(file_path)
        assert md.parse() == {'trigger': 'keyword', 'replace': 'it ==== contains ==== sep====arator\n\n```\nif bla:\n    raise ...  # <=================== here\n```'}
