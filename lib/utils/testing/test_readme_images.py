import os
import re

def check_readme_images(image_file_types: list = ['png', 'jpg', 'jpeg'], image_dir: str = 'documents/images', documents_dir: str = 'documents'):
    """
    Check that all image files in the image_dir are linked in the markdown files in documents_dir.

    Args:
        image_file_types: List of image file types to check for metadata.
        image_dir: Directory containing image files to check.
        documents_dir: Directory containing markdown files to check for image links.
    """
    image_objects = os.listdir(image_dir)
    image_dirs = [object for object in image_objects if os.path.isdir(os.path.join(image_dir, object))]
    image_files = []
    for dir in image_dirs:
        for file in os.listdir(os.path.join(image_dir, dir)):
            if file.endswith(tuple(image_file_types)):
                image_files.append(f'{image_dir}/{dir}/{file}')

    document_objects = os.listdir(documents_dir)
    markdown_files = [f'{documents_dir}/{object}' for object in document_objects if (os.path.isfile(f'{documents_dir}/{object}') and object.endswith('.md'))]
    linked_images = []
    for file in markdown_files:
        with open(file, 'r') as open_file:
            file_content = open_file.read()
            if any(image_type in file_content for image_type in image_file_types):
                regex = re.compile(r'\((?P<data>\S*)\)')
                matches = re.findall(regex, file_content)
                for match in matches:
                    if match not in linked_images:
                        linked_images.append(f'{documents_dir}/{match}')

    print('Checking that all image files are linked in the markdown files.')

    for file in image_files:
        assert file in linked_images, f'{file} not found in any markdown files.'

if __name__ == '__main__':
    check_readme_images()
