from django.http import HttpResponse
from django.shortcuts import render

from image_converter.forms import ImageConverterForm
from image_converter.utils.convert_image import convert_image_to_jpeg
from image_converter.utils.filename import get_filename_without_extension


def upload_and_convert_image_file(request):
    """
    The main view which accepts a file via an 'ImageConverterForm', converts it to a JPEG file and returns it ready for
    download as an attachment.
    """
    if request.method == 'POST':
        form = ImageConverterForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            context = {
                'file': f,
            }
            try:
                converted_img = convert_image_to_jpeg(f)
                name = get_filename_without_extension(f.name)
                response = HttpResponse(converted_img.getvalue(),
                                        content_type='image/jpeg')
                response['Content-Disposition'] = 'attachment; filename={0}.jpg'.format(name)
                return response
            except IOError:
                return render(request,'unsupported_image_file_error.html',
                              context)
            except Exception as e:
                return render(request,'generic_error.html',
                              context)
    else:
        form = ImageConverterForm()
    return render(request,
                  'upload.html',
                  {'form': form})
