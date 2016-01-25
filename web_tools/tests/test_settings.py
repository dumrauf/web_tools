from django.conf import settings
from django.test import TestCase

__author__ = 'dominic'


class DjangoSettingsTestCase(TestCase):
    """
    Tests the django 'settings'.
    """
    def test_secret_key_present(self):
        """
        Tests that the 'SECRET_KEY' attribute is defined in the 'settings'.
        """
        self.assertIsNotNone(getattr(settings, 'SECRET_KEY', None))

    def test_secret_key_non_empty(self):
        """
        Tests that the 'SECRET_KEY' attribute is well-defined.
        """
        self.assertTrue(settings.SECRET_KEY)
