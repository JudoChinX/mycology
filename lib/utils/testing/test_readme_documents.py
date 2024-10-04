# This script checks that all recipe and resource files are listed in the root README.md file.
import os

def check_readme_documents(readme_file: str, document_directories: list) -> None:
    """
    Check that all recipe and resource files are listed in the root README.md file.

    Args:
        readme_file: The README.md file to check.
        document_directories: A list of directories to check for files.
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
        assert file in file_contents, f'{file} not found in README.md'
