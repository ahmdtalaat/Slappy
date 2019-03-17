import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pain_Killer.settings')
app = Celery('Pain_Killer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
