# Generated by Django 5.1.3 on 2024-12-10 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_seedrequest_agronomist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seedrequest',
            name='pickup_date',
        ),
        migrations.RemoveField(
            model_name='seedrequest',
            name='response_date',
        ),
        migrations.RemoveField(
            model_name='seedrequest',
            name='status',
        ),
    ]
