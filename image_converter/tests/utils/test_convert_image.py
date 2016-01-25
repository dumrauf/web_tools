from cStringIO import StringIO

from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

from image_converter.tests.base import ImageConversionBaseTestCase

from image_converter.utils.convert_image import convert_image_to_jpeg, KNOWN_IMAGE_FORMATS

__author__ = 'Dominic Dumrauf'


class ImageConversionTestCase(ImageConversionBaseTestCase):
    """
    Tests the functions in the 'utils.convert_image' module.
    """
    def _convert_file(self, filename, format):
        with open(filename) as f:
            img = Image.open(f)
            converted_img = StringIO()
            img.save(converted_img, format=format)
        return converted_img

    def test_image_conversion_for_non_image_file(self):
        """
        Tests converting the 'self.non_image_file_path' which is expected to fail.
        """
        # Given
        with open(self.non_image_file_path) as f:
            # When, Then
            self.assertRaises(IOError, convert_image_to_jpeg, f)

    def test_image_conversion_for_image_file(self):
        """
        Tests converting the 'self.image_file_path' to PNG.
        """
        # Given
        with open(self.image_file_path) as f:
            # When
            result = convert_image_to_jpeg(f)
            img = Image.open(result)
            # Then
            self.assertEqual(JpegImageFile.format, img.format)
        self.assertEqual(self._convert_file(self.image_file_path, JpegImageFile.format).getvalue(),
                         result.getvalue())

    def test_known_formats(self):
        self.assertTrue(JpegImageFile.format in KNOWN_IMAGE_FORMATS)
        self.assertEqual(JpegImageFile.format,
                         KNOWN_IMAGE_FORMATS[JpegImageFile.format])
