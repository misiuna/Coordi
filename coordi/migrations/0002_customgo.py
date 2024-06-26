# Generated by Django 5.0.4 on 2024-04-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('flowChart', 'flowChart'), ('kwl', 'kwl'), ('twoCol', 'towCol'), ('causeEffect', 'causeEffect')], default='', max_length=64)),
                ('name', models.CharField(default='', max_length=64)),
                ('numRows', models.IntegerField(blank=True, null=True)),
                ('col1Title', models.CharField(default='', max_length=64)),
                ('col2Title', models.CharField(default='', max_length=64)),
            ],
        ),
    ]
