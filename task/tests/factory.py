import random
from faker import Faker

from task.models import Task, Date

fake = Faker()


def task_factory(**kwargs):
    date = kwargs.pop('date', None)
    if not date:
        date, created = Date.objects.get_or_create(date=fake.date_this_year())
    return Task.objects.create(
        date=date,
        content=fake.sentence(),
        completed=random.random() <= 0.25,
        severity=fake.random_int(min=Task.SEVERITY_LOW, max=Task.SEVERITY_HIGH),
    )
