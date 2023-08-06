from django.conf import settings
from django.utils.module_loading import import_string


def current_user_none():
    return None


# A function that returns the user who made the request.
# NOTE: function must not have arguments.
HISTORY_GET_CURRENT_USER = getattr(settings, 'HISTORY_GET_CURRENT_USER', current_user_none)

if HISTORY_GET_CURRENT_USER is not current_user_none and not callable(HISTORY_GET_CURRENT_USER):
    HISTORY_GET_CURRENT_USER = import_string(HISTORY_GET_CURRENT_USER)

# If true then the history object will be saved asynchronously using celery_app.
# WARNING: history recording uses pickle serializer.
HISTORY_ALLOW_CELERY = getattr(settings, 'HISTORY_ALLOW_CELERY', False)

# If you are deleting objects programmatically,
# pass in a list of field names that store information about deleting the object
# to more accurately create a history object.
HISTORY_SOFT_DELETE_FIELDS = getattr(settings, 'HISTORY_SOFT_DELETE_FIELDS', [])
