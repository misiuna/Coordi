# Generated by Django 5.0.4 on 2024-05-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordi', '0015_assignments_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='graded',
            field=models.DateTimeField(blank=True, null=True, verbose_name='graded'),
        ),
    ]
