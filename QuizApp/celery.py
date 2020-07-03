from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

# setting environment variables default for django settings module i.e, referencing settings file in our QuizApp project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QuizApp.settings')

app = Celery('QuizApp')

# Using project settings file as our configuration file so that all configuration live in one place
app.config_from_object('django.conf:settings')

# Auto discover tasks.py file in every application for this project
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
