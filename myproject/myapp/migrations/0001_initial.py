# Generated by Django 5.1.3 on 2024-12-05 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agronomist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed', models.CharField(blank=True, max_length=100, null=True)),
                ('fertilizer', models.CharField(blank=True, max_length=100, null=True)),
                ('seedquantity', models.IntegerField(blank=True, null=True)),
                ('fertilizerquantity', models.IntegerField(blank=True, null=True)),
                ('planting_season', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(null=True)),
            ],
            options={
                'unique_together': {('contact',)},
            },
        ),
        migrations.CreateModel(
            name='FertilizerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('response_date', models.DateField(blank=True, null=True)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('agronomist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.agronomist')),
            ],
        ),
        migrations.CreateModel(
            name='SeedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('response_date', models.DateField(blank=True, null=True)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('agronomist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.agronomist')),
            ],
        ),
    ]
