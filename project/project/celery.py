from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'sync-currency-snapshot-daily': {
        'task': 'currencies.tasks.sync_currency_snapshot',
        'schedule': crontab(minute='*/1') # Change to daily
    },
}

app.autodiscover_tasks()
