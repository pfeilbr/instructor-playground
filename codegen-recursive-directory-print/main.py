import argparse
import os


def print_directory_contents(path):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print files and directories in a directory')
    parser.add_argument('directory', type=str, help='Absolute directory path')
    args = parser.parse_args()
    print_directory_contents(args.directory)
