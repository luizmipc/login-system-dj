#!/bin/sh

chown -R duser:duser .
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000