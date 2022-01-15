from django.db import models
from django.urls import reverse


class Date(models.Model):
    date = models.DateField(unique=True, primary_key=True)

    def get_absolute_url(self):
        return reverse('task:date', kwargs={'date': self.date.strftime('%Y-%m-%d')})

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)


class Task(models.Model):
    SEVERITY_LOW = 0
    SEVERITY_MEDIUM = 1
    SEVERITY_HIGH = 2

    SEVERITY_CHOICES = [
        (SEVERITY_LOW, 'Low'),
        (SEVERITY_MEDIUM, 'Medium'),
        (SEVERITY_HIGH, 'High'),
    ]

    content = models.TextField(max_length=255)
    time = models.TimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    severity = models.IntegerField(choices=SEVERITY_CHOICES, default=SEVERITY_LOW)
    date = models.ForeignKey(
        Date, on_delete=models.CASCADE, related_name='tasks', blank=True
    )

    def toggle_completed(self):
        self.completed = not self.completed
        self.save()

    def get_absolute_url(self):
        return reverse('task:update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.content
