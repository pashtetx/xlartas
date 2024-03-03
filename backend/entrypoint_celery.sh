#!/bin/sh
echo "#####################################"
echo "######### Celery Starting... ########"
echo "#####################################"
python manage.py migrate

# Инициализация Django
# shellcheck disable=SC2164
cd /srv/backend

python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'); import django; django.setup()"
echo "django inited for celery"

sleep 1

celery -A config worker --loglevel=warning --task-events -E
