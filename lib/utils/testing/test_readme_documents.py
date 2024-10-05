from lib import file_utils


def check_readme_documents(readme_file: str, document_file_types: list, document_directories: list) -> None:
    """
    Check that all recipe and resource files are listed in the root README.md file.

    Args:
        readme_file: The README.md file to check for all recipe and resource files.
        document_file_types: A list of file types to check for in the README.md file.
        document_directories: A list of directories to check for files.
    """
    documents_to_check = file_utils.find_files_with_extensions(document_directories, document_file_types)

    if not documents_to_check:
        print('No files found in the recipe directories.')

    else:
        with open(readme_file, 'r', encoding='utf8') as file:
            file_contents = file.read()

        print(f'Checking {readme_file} for all recipe and resource files.')

        for file in documents_to_check:
            assert file in file_contents, f'{file} not found in README.md'
