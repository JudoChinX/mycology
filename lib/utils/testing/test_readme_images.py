import re

from lib import file_utils


def check_readme_images(image_file_types: list, image_dirs: list, document_file_types: list, documents_dirs: list) -> None:
    """
    Check that all image_file_types in the image_dir are linked in the document_file_types in documents_dir.

    Args:
        image_file_types: List of image file types to check for metadata.
        image_dir: Directory containing image files to check.
        document_file_types: List of document file types to check for image links.
        documents_dir: Directory containing document_file_types to check for image links.
    """
    image_files = file_utils.find_files_with_extensions(image_dirs, image_file_types)
    markdown_files = file_utils.find_files_with_extensions(documents_dirs, document_file_types)
    linked_images = []
    for file in markdown_files:
        parent_dir = file.split('/')[0]
        with open(file, 'r', encoding='utf8') as open_file:
            file_content = open_file.read()
            regex = re.compile(r'\((?P<data>\S*)\)')
            matches = re.findall(regex, file_content)
            for match in matches:
                if match not in linked_images:
                    linked_images.append(f'{parent_dir}/{match}')

    if not image_files:
        print('No image files found in the specified image_dirs.')
    elif not linked_images:
        print('No image files linked in the specified document_file_types.')
    else:
        print('Checking that all image files are linked in the specified document_file_types.')

        for file in image_files:
            assert file in linked_images, f'{file} not found in any specified document_file_types.'
