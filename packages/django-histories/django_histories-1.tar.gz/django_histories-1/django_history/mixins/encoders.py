from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class JSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Model):
            return obj.pk

        return super().default(obj)
