import os
import re
from lib import file_utils

def check_readme_images(image_file_types: list = ['png', 'jpg', 'jpeg'], image_dirs: list = ['documents/images'], document_file_types: list = ['.md'], documents_dirs: list = ['documents']):
    """
    Check that all image files in the image_dir are linked in the markdown files in documents_dir.

    Args:
        image_file_types: List of image file types to check for metadata.
        image_dir: Directory containing image files to check.
        documents_dir: Directory containing markdown files to check for image links.
    """
    image_files = file_utils.find_files_with_extensions(image_dirs, image_file_types)
    markdown_files = file_utils.find_files_with_extensions(documents_dirs, document_file_types)
    linked_images = []
    for file in markdown_files:
        parent_dir = file.split('/')[0]
        with open(file, 'r') as open_file:
            file_content = open_file.read()
            regex = re.compile(r'\((?P<data>\S*)\)')
            matches = re.findall(regex, file_content)
            for match in matches:
                if match not in linked_images:
                    linked_images.append(f'{parent_dir}/{match}')

    print('Checking that all image files are linked in the markdown files.')

    for file in image_files:
        assert file in linked_images, f'{file} not found in any markdown files.'

if __name__ == '__main__':
    check_readme_images()
