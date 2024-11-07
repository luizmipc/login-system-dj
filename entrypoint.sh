#!/bin/sh

# Run migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000