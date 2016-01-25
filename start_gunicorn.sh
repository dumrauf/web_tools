#!/bin/bash

source virtualenv_utils.sh
activate_virtualenv

echo "Starting gunicorn with the following configuration..."
echo "------------------------------------------------------------------------------------"
cat gunicorn.conf.py
echo "------------------------------------------------------------------------------------"
echo "To stop the server just type Ctrl-C as you would with the django test server"

gunicorn -c gunicorn.conf.py web_tools.wsgi:application --pid logs/gunicorn.pid #--daemon
