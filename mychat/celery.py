from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

app = Celery('mychat')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def email(self,verifyurl):
	print('Verification Link: ', 'http://127.0.0.1:8000/user/',verifyurl)
	return (verifyurl)
    # send_mail(
    # 'Verification Link',
    # verify,
    # 'mahtaakhyani@gmail.com',
    # [email],
    # fail_silently=False,
    # 	)

