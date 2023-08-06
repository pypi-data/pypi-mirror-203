# django_history

Django_history - a module for tracking changes to model instances.

# Install

```
pip3 install git+https://github.com/QuantumaStelata/django-history.git
```

# Add to INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    'django_history'
    ...
]
```

# Do migrations

```
python3 manage.py migrate
```

# Create a model

```
class Task(models.Model):
  ...
```


# Add mixin to your model

```
from django_history.mixins import HistoryMixin


class Task(HistoryMixin):
  ...
```

> Note: `using a HistoryMixin` doesn't need to be migrated

**Congrats, history is being recorded**

# For flexible use, write in the settings.py

```
# A function that returns the user who made the request.
# NOTE: function must not have arguments.
HISTORY_GET_CURRENT_USER

# If true then the history object will be saved asynchronously using celery_app.
# WARNING: history recording uses pickle serializer.
HISTORY_ALLOW_CELERY

# If you are deleting objects programmatically,
# pass in a list of field names that store information about deleting the object
# to more accurately create a history object.
HISTORY_SOFT_DELETE_FIELDS

```

# For example

1) Using soft delete model

```
# models.py
class Task(HistoryMixin):
  ...
  deleted_at = models.DateTimeField(null=True)
  ...

# settings.py
# Pass soft delete field in HISTORY_SOFT_DELETE_FIELDS
HISTORY_SOFT_DELETE_FIELDS = ['deleted_at']
```

2) If you use [django-currentuser](https://github.com/PaesslerAG/django-currentuser), pass get_current_user function to HISTORY_GET_CURRENT_USER
```
# settings.py
from django_currentuser.middleware import get_current_user

HISTORY_GET_CURRENT_USER = get_current_user
```
