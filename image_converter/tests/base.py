import os
from django.conf import settings
from django.test import TestCase

__author__ = 'dominic'


class ImageConversionBaseTestCase(TestCase):
    """
    A base class for all django TestCases that require access to image and non-image test files.
    """
    def setUp(self):
        self.base_data_dir = os.path.join(settings.BASE_DIR, 'image_converter', 'tests', 'data')
        self.image_file_name = 'image'
        self.image_file_extension = 'png'
        self.image_file_path = os.path.join(self.base_data_dir, '{0}.{1}'.format(self.image_file_name,
                                                                                 self.image_file_extension))
        self.non_image_file_name = 'non_image_file'
        self.non_image_file_path = os.path.join(self.base_data_dir, self.non_image_file_name)
