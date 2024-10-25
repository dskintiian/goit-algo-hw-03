import os.path
import sys
import shutil
from os import listdir, path, makedirs

def copy_dir_item(source_dir: str, dest_dir: str) -> None:
    try:
        for dir_item in listdir(source_dir):
            if path.islink(source_dir + '/' + dir_item):
                print(f'Links are not suppoerted')
            elif path.isfile(source_dir + '/' + dir_item):
                copy_file(source_dir.rstrip('/') + '/' + dir_item, path.abspath(dest_dir))
            elif path.isdir(source_dir + '/' + dir_item):
                copy_dir_item(source_dir.rstrip('/') + '/' + dir_item, path.abspath(dest_dir))

    except FileNotFoundError:
        print(f'Directory {source_dir} is not found')
    except PermissionError:
        print(f'Cannot read directory {source_dir}')
    except NotADirectoryError:
        print(f'{source_dir} is not a directory')

def copy_file(from_path: str, dest_dir: str) -> None:
    print(from_path, dest_dir)
    if not path.isdir(dest_dir):
        makedirs(dest_dir)

    _, file_extension = os.path.splitext(from_path)
    file_extension = file_extension.lstrip('.')
    if not path.isdir(dest_dir + '/' + file_extension):
        makedirs(dest_dir + '/' + file_extension)

    shutil.copy(from_path, dest_dir + '/' + file_extension + '/')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('source directory must be provided')
        exit(0)

    copy_dir_item(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'dist')