# Generated by Django 5.0.4 on 2024-04-28 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordi', '0002_customgo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgo',
            name='type',
            field=models.CharField(choices=[('flowChart', 'flowChart'), ('kwl', 'kwl'), ('twoCol', 'twoCol'), ('causeEffect', 'causeEffect')], default='', max_length=64),
        ),
    ]