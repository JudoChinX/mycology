import os
from PIL import Image

def check_image_metadata(image_file_types: list = ['png', 'jpg', 'jpeg'], image_dir: str = 'documents/images'):
    image_objects = os.listdir(image_dir)
    image_dirs = [object for object in image_objects if os.path.isdir(os.path.join(image_dir, object))]
    image_files = []
    for dir in image_dirs:
        for file in os.listdir(os.path.join(image_dir, dir)):
            if file.endswith(tuple(image_file_types)):
                image_files.append(f'{image_dir}/{dir}/{file}')

    print('Checking image metadata for all image files.')

    for file in image_files:
        open_file = Image.open(file)
        metadata = open_file._getexif()
        if metadata:
            print(f'Metadata for {file}: {metadata}')

if __name__ == '__main__':
    check_image_metadata()
