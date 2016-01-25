#!/bin/bash

source virtualenv_utils.sh
activate_virtualenv

python manage.py test -v 3 image_converter/tests web_tools/tests
