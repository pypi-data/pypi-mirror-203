from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import post_delete, post_init, post_save
from django.forms import model_to_dict

from django_history.models import History
from django_history.settings import (
    HISTORY_ALLOW_CELERY, HISTORY_GET_CURRENT_USER,
    HISTORY_SOFT_DELETE_FIELDS,
)
from django_history.tasks import history as tasks
from django_history.utils import get_instance_changes


class HistoryMixin(models.Model):
    INIT_INSTANCE_DICT = '_init_instance_dict'

    histories = GenericRelation(
        History,
        content_type_field='content_type',
        object_id_field='object_id',
        related_query_name='%(class)s',
    )

    class Meta:
        abstract = True

    @classmethod
    def history_post_init(cls, instance, *args, **kwargs):
        setattr(instance, cls.INIT_INSTANCE_DICT, model_to_dict(instance))

    @classmethod
    def history_post_save(cls, sender, instance, created, *args, **kwargs):
        if any(bool(getattr(instance, field, False)) for field in HISTORY_SOFT_DELETE_FIELDS):
            return post_delete.send(sender=sender, instance=instance)

        history_kw = {}

        if HISTORY_GET_CURRENT_USER:
            history_kw['author_id'] = (author := HISTORY_GET_CURRENT_USER()) and author.id or None

        history_kw['content_object'] = instance
        history_kw['pre_instance'] = getattr(instance, cls.INIT_INSTANCE_DICT, None) if not created else None
        history_kw['post_instance'] = model_to_dict(instance)
        history_kw['state'] = kwargs.get(
            'state',
            created and History.StateChoices.CREATED or History.StateChoices.UPDATED,
        )

        if not created:
            history_kw['instance_changes'] = get_instance_changes(
                history_kw['pre_instance'],
                history_kw['post_instance'],
            )

        if history_kw['pre_instance'] != history_kw['post_instance']:
            if HISTORY_ALLOW_CELERY:
                tasks.create_history.delay(**history_kw)
            else:
                tasks.create_history(**history_kw)

            post_init.send(sender=sender, instance=instance)

    @classmethod
    def history_m2m_changed(cls, instance, action, *args, **kwargs):
        if action.startswith('post_'):
            post_save.send(sender=cls, instance=instance, created=False, state=History.StateChoices.M2M_UPDATED)

    @classmethod
    def history_post_delete(cls, instance, *args, **kwargs):
        history_kw = {}

        if HISTORY_GET_CURRENT_USER:
            history_kw['author_id'] = (author := HISTORY_GET_CURRENT_USER()) and author.id or None

        history_kw['content_object'] = instance
        history_kw['pre_instance'] = getattr(instance, cls.INIT_INSTANCE_DICT, None)
        history_kw['state'] = History.StateChoices.DELETED

        if HISTORY_ALLOW_CELERY:
            tasks.create_history.delay(**history_kw)
        else:
            tasks.create_history(**history_kw)
