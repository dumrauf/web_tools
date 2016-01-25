from random import choice
from string import letters

from django.test import TestCase

from image_converter.utils.filename import get_filename_without_extension

__author__ = 'Dominic Dumrauf'


class FilenameTestCase(TestCase):
    """
    Tests the functions in the 'utils.filename' module.
    """
    def test_empty_filename(self):
        """
        Tests an empty file name.
        """
        # Given
        expected_name = 'file'
        # When
        name = get_filename_without_extension('')
        # Then
        self.assertEqual(expected_name,
                         name)

    def test_filename_without_extension(self):
        """
        Tests random file names that lack an extension.
        """
        for _ in xrange(100):
            # Given
            expected_filename = ''.join([choice(letters) for _ in xrange(8)])
            # When
            name = get_filename_without_extension(expected_filename)
            # Then
            self.assertEqual(expected_filename,
                             name)

    def test_multiple_extensions(self):
        """
        Tests random file names with multiple extensions.
        """
        for _ in xrange(100):
            # Given
            filename = ''.join([choice(letters) for _ in xrange(8)])
            for _ in xrange(10):
                filename += '.'.join([choice(letters) for _ in xrange(3)])
            # When
            name = get_filename_without_extension(filename)
            # Then
            expected_name, extension = filename.rsplit('.', 1)
            self.assertEqual(expected_name,
                             name)

    def test_standard_filename(self):
        """
        Tests random file names which are made up of a name without any dots and a single extension; name and
        extension are separated by a dot.
        """
        for _ in xrange(100):
            # Given
            expected_name = ''.join([choice(letters) for _ in xrange(8)])
            extension = ''.join([choice(letters) for _ in xrange(3)])
            filename = '{0}.{1}'.format(expected_name,
                                        extension)
            # When
            name = get_filename_without_extension(filename)
            # Then
            self.assertEqual(expected_name,
                             name)
