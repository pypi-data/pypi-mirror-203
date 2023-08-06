import argparse

from obsidian import ObsidianParser


def main():
    parser = argparse.ArgumentParser(description='Parse Obsidian markdown files')
    parser.add_argument('md_dir', type=str, help='Directory where the markdown files are located')
    parser.add_argument('--per-project', action='store_true', help='Generate a yaml file per project', default=True)
    args = parser.parse_args()
    obsidian_parser = ObsidianParser(args.md_dir, args.per_project)
    matches = obsidian_parser.generate_matches()
    obsidian_parser.write_yamls(matches)
