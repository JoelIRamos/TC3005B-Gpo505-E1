import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API_PROJECT.settings')
 
app = Celery('API_PROJECT')
app.config_from_object('django.conf:settings')


 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()