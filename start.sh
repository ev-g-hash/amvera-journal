#!/bin/sh
# start.sh
set -e

echo "Apply migrations..."
python manage.py migrate --noinput

echo "Collect static (already done in build, but safe to re-run)..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 60 --keep-alive 2 --max-requests 1000 --max-requests-jitter 100