# Generated by Django 5.0.4 on 2024-05-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordi', '0011_data_assignment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='answer1',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer10',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer2',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer3',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer4',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer5',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer6',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer7',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer8',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='answer9',
            field=models.CharField(blank=True, default='', max_length=650, null=True),
        ),
    ]
