from django.test import Client
import mock as mock

from image_converter.tests.base import ImageConversionBaseTestCase
from image_converter.utils.convert_image import convert_image_to_jpeg

__author__ = 'Dominic Dumrauf'


class ViewsTestCase(ImageConversionBaseTestCase):
    """
    Tests the 'views'.
    """
    def test_upload_get(self):
        """
        Tests GETting the form initially.
        """
        # Given
        c = Client()
        # When
        response = c.get('/')
        # Then
        self.assertTemplateUsed(response, template_name='upload.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_upload_post_without_file(self):
        """
        Tests POSTing a form which *lacks* a file.
        """
        # Given
        c = Client()
        # When
        response = c.post('/')
        # Then
        self.assertTemplateUsed(response, template_name='upload.html')
        self.assertFormError(response, 'form', 'file', 'This field is required.')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_upload_post_with_non_image_file(self):
        """
        Tests POSTing a form which contains a file but the file is not an image.
        """
        # Given
        c = Client()
        # When
        with open(self.non_image_file_path) as fp:
            response = c.post('/', {'file': fp})
        # Then
        self.assertTemplateUsed(response, template_name='unsupported_image_file_error.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('file', response.context)
        self.assertIn(self.non_image_file_name, response.content)

    def test_upload_post_with_image_file(self):
        """
        Tests POSTing a form which contains a file where the file is an image.
        """
        # Given
        c = Client()
        # When
        with open(self.image_file_path) as fp:
            response = c.post('/', {'file': fp})
            converted_image = convert_image_to_jpeg(fp)
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename={0}.jpg'.format(self.image_file_name))
        self.assertEqual(response.content, converted_image.getvalue())

    @mock.patch('image_converter.views.convert_image_to_jpeg')
    def test_unexpected_error_in_image_conversion_handling(self, convert_image_to_jpeg):
        """
        Tests POSTing a form where converting the image raises an unexpected exception.
        """
        # Given
        convert_image_to_jpeg.side_effect = Exception()
        c = Client()
        # When
        with open(self.non_image_file_path) as fp:
            response = c.post('/', {'file': fp})
        # Then
        self.assertTemplateUsed(response, template_name='generic_error.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('file', response.context)
        self.assertIn(self.non_image_file_name, response.content)
