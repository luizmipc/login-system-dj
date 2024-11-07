#!/bin/sh

# Run migrations
python manage.py makemigrations accounts
python manage.py migrate

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000