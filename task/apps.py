from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'task'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from task.signals import task_pre_save, task_post_delete
