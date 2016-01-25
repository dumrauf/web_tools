# About the 'web_tools' Project

A collection of web tools written in django.

Currently, the _'web_tools'_ project only features the _image converter_ app as described in the next section. 



# The Image Converter App

This app was sparked by [WhatsApp](https://www.whatsapp.com/) refusing to accept any non-[JPEG](https://en.wikipedia.org/wiki/JPEG) image and no 
conversion app installed on the phone.

The 'image_converter' app offers a simple website with a form where [image files](https://en.wikipedia.org/wiki/Image_file_formats) can be uploaded. The uploaded image 
file is converted to [JPEG](https://en.wikipedia.org/wiki/JPEG) and eventually returned as a download.



# Getting Started

Please make sure you have at least Python 2.7 installed. 


## Batteries Included

Bootstrap the environment with

```
./bootstrap_environment.sh
```

This will install a virtual environment in `../virtualenvs/web_tools`

_Note_: For security reasons, you need to update the `SECRET_KEY` in `web_tools/private_settings.py` with _your_ 
private key, as django will complain otherwise.


# Verify Things are Correct

Run all test with 

```
./run_all_tests.sh
```

and verify that they are passing without any errors.


## See it in Action

Start the django test server with

```
./run_test_server.sh
```

and surf to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Note that the address is defined in the script as a parameter 
passsed to the django `manage.py` command.


## Deploying

There is also a rudimentary [Gunicorn](http://gunicorn.org/) configuration provided in `gunicorn_conf.py`, in case 
you want to eventually run it behind an [Nginx](https://www.nginx.com/). For that, use the command

```
./start_gunicorn.sh
```