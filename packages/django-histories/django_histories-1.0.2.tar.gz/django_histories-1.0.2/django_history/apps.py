from django.apps import AppConfig


class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_history'

    def ready(self):
        from django.db.models.signals import (
            m2m_changed, post_delete,
            post_init, post_save,
        )

        from django_history.mixins import HistoryMixin

        for cls in self.all_subclasses(HistoryMixin):
            post_init.connect(cls.history_post_init, sender=cls)
            post_save.connect(cls.history_post_save, sender=cls)
            post_delete.connect(cls.history_post_delete, sender=cls)

            for field in cls._meta.many_to_many:
                relation = getattr(cls, field.name)
                through = getattr(relation, 'through')

                m2m_changed.connect(cls.history_m2m_changed, sender=through)

    def all_subclasses(self, cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in self.all_subclasses(c)],
        )
