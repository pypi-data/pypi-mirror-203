from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from django_history.mixins.encoders import JSONEncoder
from django_history.settings import HISTORY_GET_CURRENT_USER


class History(models.Model):
    class StateChoices(models.TextChoices):
        CREATED = ('created', 'Created')
        UPDATED = ('updated', 'Updated')
        M2M_UPDATED = ('m2m_updated', 'M2M Updated')
        DELETED = ('deleted', 'Deleted')

    state = models.CharField(max_length=12, choices=StateChoices.choices, default=StateChoices.CREATED)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.TextField()
    content_object = GenericForeignKey('content_type', 'object_id')
    pre_instance = models.JSONField(null=True, encoder=JSONEncoder)
    post_instance = models.JSONField(null=True, encoder=JSONEncoder)
    instance_changes = models.JSONField(null=True, encoder=JSONEncoder)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        default=HISTORY_GET_CURRENT_USER,
    )

    class Meta:
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]
