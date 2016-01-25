from cStringIO import StringIO
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

__author__ = 'dominic'

_FORMAT_JPEG = JpegImageFile.format

_IMAGE_FORMATS = [
    _FORMAT_JPEG
]

KNOWN_IMAGE_FORMATS = dict(zip(_IMAGE_FORMATS, _IMAGE_FORMATS))


def _convert_image(image, format):
    img = Image.open(image)
    converted_img = StringIO()
    img.save(converted_img, format=format)
    return converted_img


def convert_image_to_jpeg(image):
    return _convert_image(image=image,
                          format=_FORMAT_JPEG)
