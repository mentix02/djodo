# Generated by Django 4.0.1 on 2022-01-14 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                (
                    'date',
                    models.DateField(primary_key=True, serialize=False, unique=True),
                ),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('content', models.TextField(max_length=255)),
                ('time', models.TimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                (
                    'severity',
                    models.IntegerField(
                        choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0
                    ),
                ),
                (
                    'date',
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='tasks',
                        to='task.date',
                    ),
                ),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
