import argparse

from lib.file_utils import find_files_with_extensions
from lib.image_utils import resize_image

def resize_images(image_directories: list, image_file_extensions: list):
    image_files = find_files_with_extensions(image_directories, image_file_extensions)
    for image in image_files:
        name = image.split('.')[0]
        extension = image.split('.')[-1]
        print(f'Resizing {image} to {name}.{extension}')
        resize_image(image, f'{name}.{extension}', 800, None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resize images in the specified directories.')
    parser.print_help()
    parser.add_argument('--image-directories', nargs='+', help='Directories containing images to resize.')
    parser.add_argument('--image-file-extensions', nargs='+', default=['.jpg', '.jpeg', '.png', '.heic'], help='Image file extensions to resize.')
    args = parser.parse_args()
    resize_images(image_directories=args.image_directories, image_file_extensions=args.image_file_extensions)
