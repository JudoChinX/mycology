# This script checks that all recipe and resource files are listed in the root README.md file.
import os

def check_files_in_readme(readme_file: str = 'README.md', document_directories: list = ['documents']) -> None:
    """
    Check that all recipe and resource files are listed in the root README.md file.

    Args:
        readme_file (str): The README.md file to check.
        document_directories (list): A list of directories to check for files.
    """
    document_objects = []
    for directory in document_directories:
        objects = os.listdir(directory)
        objects = [f'{directory}/{object}' for object in objects]
        document_objects.extend(objects)
    files_to_check = [file for file in document_objects if os.path.isfile(file)]

    if not files_to_check:
        print('No files found in the recipe directory.')

    with open(readme_file, 'r') as file:
        file_contents = file.read()

    print('Checking README.md for all recipe and resource files.')

    for file in files_to_check:
        if ' ' in file:
            # Replace spaces in filename with %20.
            file = file.replace(' ', '%20')
        assert file in file_contents, f'{file} not found in README.md'

if __name__ == '__main__':
    check_files_in_readme()
