# Generated by Django 5.1.3 on 2024-12-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_agronomist_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agronomist',
            name='contact_info',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
