#!/usr/bin/env python3
import csv
from pathlib import Path
from argparse import ArgumentParser
from os import getcwd
from sys import exit

from pyexcel_ods3 import get_data


def get_args():
    parser = ArgumentParser(
        prog='ods-to-csv',
        description='Convert from .ods to .csv ',
    )

    parser.add_argument(
        'ods_file',
        metavar='FILE',
        type=Path,
        help='.ods file.',
    )

    parser.add_argument(
        '-d',
        '--dest',
        type=Path,
        help='Destination directory, optional.',
        default=Path(getcwd()),
    )

    return parser.parse_args()


def convert(path: Path, dest: Path):
    data = get_data(str(path))

    for sheet_name, rows in data.items():
        if not rows:
            continue

        output_path = dest / f"{path.stem}-{sheet_name}.csv'"
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print(f"Saved '{path.name}'#'{sheet_name}' to '{output_path}'")


def main():
    args = get_args()

    ods: Path = args.ods_file
    if not ods.exists():
        print(f"ODS file not found: {ods}")
        exit(1)

    dest: Path = args.dest
    if not dest.exists() or not dest.is_dir():
        print(f"Destination directory not found: {dest}")

    convert(ods, dest)
    exit(0)


if __name__ == "__main__":
    main()
