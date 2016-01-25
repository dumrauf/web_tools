from cStringIO import StringIO
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

__author__ = 'dominic'

# A constant for the JPEG image format
_FORMAT_JPEG = JpegImageFile.format

# A list of image formats
_IMAGE_FORMATS = [
    _FORMAT_JPEG
]

# A dictionary of known image formats
KNOWN_IMAGE_FORMATS = dict(zip(_IMAGE_FORMATS, _IMAGE_FORMATS))


def _convert_image(image, format):
    """
    Converts the given 'image' to the supplied 'format' and returns the result.

    Raises an exception in case the 'image' is not a valid image file.

    :param image: the image to convert
    :param format: the format to convert the image to
    :return: the converted image as a StringIO object
    """
    img = Image.open(image)
    converted_img = StringIO()
    img.save(converted_img, format=format)
    return converted_img


def convert_image_to_jpeg(image):
    """
    Converts the given 'image' to JPEG and returns it as an in-memory file

    :param image: the image to convert
    :return: the converted JPEG image as a StringIO object
    """
    return _convert_image(image=image,
                          format=_FORMAT_JPEG)
