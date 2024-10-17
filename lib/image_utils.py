import pillow_heif
import qrcode
from PIL import Image


def create_qr_code(data: str, output_path: str) -> None:
    """
    Create a QR code from the specified data and save it to a file.

    Args:
        data: Data to store in the QR code.
        output_path: Path to save the QR code.
    """
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=False)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(output_path)

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
    if cur_width == width and cur_height == height:
        print('Image is already the specified size. Skipping.')
    else:
        if output_path.endswith('.heic'):
            pillow_heif.from_pillow(resized_image).save(output_path)
        else:
            resized_image.save(output_path)

def remove_metadata(image_path: str, output_path: str) -> None:
    """
    Remove metadata from an image and save it to a new file.

    Args:
        image_path: Path to the image to remove metadata from.
        output_path: Path to save the image without metadata.
    """
    if image_path.endswith('.heic'):
        image = pillow_heif.open_heif(image_path)
        image = image.to_pillow()
    else:
        image = Image.open(image_path)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    if output_path.endswith('.heic'):
        pillow_heif.from_pillow(image_without_exif).save(output_path)
    else:
        image_without_exif.save(output_path)
