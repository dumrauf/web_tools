__author__ = 'dominic'


def get_filename_without_extension(filename):
    """
    Returns the name of the 'filename', removing any extension. Here, an extension is indicated by a *dot*,
    e.g. 'file.txt' where 'file' denotes the name and 'txt' is the extension.

    If multiple extensions exist, only the last one is removed. In case no extension is present, the entire
    'filename' is returned.

    In case the 'filename' is empty, the string 'file' is returned.

    :param filename: the filename to get the name from
    :return: the name of the given 'filename'
    """
    if not filename:
        return 'file'
    try:
        name, extension = filename.rsplit('.', 1)
        return name
    except ValueError:
        return filename
