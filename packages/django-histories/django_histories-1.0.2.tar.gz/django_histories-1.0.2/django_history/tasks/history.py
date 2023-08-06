from celery import current_app
from django.apps import apps


@current_app.task(serializer='pickle')
def create_history(*args, **kwargs):
    return apps.get_model('django_history.History').objects.create(*args, **kwargs)
