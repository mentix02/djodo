from django.dispatch import receiver
from django.utils.timezone import now, localtime
from django.db.models.signals import pre_save, post_delete

from task.models import Task, Date


# Make sure a date exists for today before saving a task
@receiver(pre_save, sender=Task)
def task_pre_save(sender, instance: Task, **kwargs):
    if not hasattr(instance, 'date'):
        today = localtime(now()).date()
        date, created = Date.objects.get_or_create(date=today)
        instance.date = date


# Delete date if no tasks are left for that date
@receiver(post_delete, sender=Task)
def task_post_delete(sender, instance: Task, **kwargs):
    if instance.date.tasks.count() == 0:
        instance.date.delete()
