import argparse
import os

from pydantic import BaseModel


class Directory(BaseModel):
    path: str


def print_directory_contents(directory: Directory):
    for root, dirs, files in os.walk(directory.path):
        level = root.replace(directory.path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recursively print the files and directories in a given directory.')
    parser.add_argument('--path', type=str, help='The absolute path of the directory to explore')
    args = parser.parse_args()

    directory = Directory(path=args.path)
    print_directory_contents(directory)
