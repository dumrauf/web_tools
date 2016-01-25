__author__ = 'dominic'

bind = '127.0.0.1:9000'                   # Don't use port 80 becaue nginx occupied it already.
name = 'web_tools'
errorlog = 'logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = 'logs/gunicorn-access.log'
loglevel = 'debug'
user = 'dominic'
workers = 2     # the number of recommended workers is '2 * number of CPUs + 1'
