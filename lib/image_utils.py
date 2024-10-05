import pillow_heif
from PIL import Image


def resize_image(image_path: str, output_path: str, width: int | None, height: int | None) -> None:
    """
    Resize an image to the specified width and height.

    Args:
        image_path: Path to the image to resize.
        output_path: Path to save the resized image.
        width: Width of the resized image.
        height: Height of the resized image.
    """
    if not width and not height:
        raise ValueError('Width or height must be specified.')
    if image_path.endswith('.heic'):
        image = pillow_heif.open_heif(image_path)
        image = image.to_pillow()
    else:
        image = Image.open(image_path)
    cur_width, cur_height = image.size
    if not width:
        width = int(cur_width * height / cur_height)
    elif not height:
        height = int(cur_height * width / cur_width)
    resized_image = image.resize((width, height))
    resized_image.save(output_path)
