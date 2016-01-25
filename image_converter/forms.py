from django.forms import Form, FileField

__author__ = 'Dominic Dumrauf'


class ImageConverterForm(Form):
    """
    A simple for that merely provides a FileField.
    """
    file = FileField(label='',
                     help_text='')
