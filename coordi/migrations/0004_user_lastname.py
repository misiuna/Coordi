# Generated by Django 5.0.4 on 2024-04-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordi', '0003_alter_customgo_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='', max_length=150),
        ),
    ]