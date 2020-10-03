#!/bin/bash
gunicorn blog.wsgi:application --bind "0.0.0.0:$PORT" --env DJANGO_SETTINGS_MODULE=blog.settings.production
