import argparse
import os

from lib.file_utils import find_files_with_extensions
from lib.image_utils import create_qr_code


def generate_qr_codes(file_directories: list, file_extensions: list, output_directory: str, domain: str):
    """ Generate QR codes for files in the specified directories.

    Args:
        file_directories: Directories containing files to generate QR codes for.
        file_extensions: File extensions of files to generate QR codes for.
        output_directory: Directory to save the QR codes.
    """
    files = find_files_with_extensions(file_directories, file_extensions)
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    for file in files:
        new = file.split('.')[0]
        newer = f'{new}-qr.png'
        newest = newer.rsplit('/', maxsplit=1)[-1]
        url = f'{domain}/{file}'
        create_qr_code(url, f'{output_directory}/{newest}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate QR codes for files in the specified directories.')
    parser.add_argument('--file-directories', nargs='+', help='Directories containing files to generate QR codes for.', required=True)
    parser.add_argument('--file-extensions', nargs='+', default=['.jpg', '.jpeg', '.png', '.heic'], help='File extensions of files to generate QR codes for.', required=True)
    parser.add_argument('--output-directory', help='Directory to save the QR codes.', required=True)
    parser.add_argument('--domain', help='Domain to prefix the QR code data with.', required=True)
    args = parser.parse_args()
    generate_qr_codes(file_directories=args.file_directories, file_extensions=args.file_extensions, output_directory=args.output_directory, domain=args.domain)
