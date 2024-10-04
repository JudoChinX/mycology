import exifread

from lib import file_utils


def check_image_metadata(image_file_types: list, image_dirs: list) -> None:
    """
    Check the metadata of all image files in the specified directory.

    Args:
        image_file_types: List of image file types to check for metadata.
        image_dirs: Directory containing image files to check.
    """
    image_files = file_utils.find_files_with_extensions(image_dirs, image_file_types)

    if not image_files:
        print('No image files found in the specified directories.')
    else:
        print('Checking image metadata for all image files.')

        for file in image_files:
            with open(file, 'rb') as open_file:
                metadata = exifread.process_file(open_file)
                if metadata:
                    print(f'\nMetadata for {file}: {metadata}\n')
