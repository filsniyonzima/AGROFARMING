# Generated by Django 5.1.3 on 2024-12-10 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_seedrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seedrequest',
            name='agronomist',
        ),
    ]
