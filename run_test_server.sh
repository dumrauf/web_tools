#!/bin/bash

source virtualenv_utils.sh
activate_virtualenv

python manage.py runserver 127.0.0.1:8000
