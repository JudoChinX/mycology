from lib.file_utils import find_files_with_extensions
from lib.image_utils import resize_image

image_files = find_files_with_extensions(['documents/images'], ['.jpg', '.jpeg', '.png'])
for image in image_files:
    name = image.split('.')[0]
    extension = image.split('.')[-1]
    print(f'Resizing {image} to {name}.{extension}')
    resize_image(image, f'{name}.{extension}', 800, None)
