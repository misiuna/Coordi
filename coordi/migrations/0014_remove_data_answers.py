# Generated by Django 5.0.4 on 2024-05-08 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coordi', '0013_data_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='answers',
        ),
    ]
