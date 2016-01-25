__author__ = 'dominic'


def get_filename_without_extension(filename):
    if not filename:
        return 'file'
    try:
        name, extension = filename.rsplit('.', 1)
        return name
    except ValueError:
        return filename
