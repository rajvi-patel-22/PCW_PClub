# Generated by Django 3.0.4 on 2020-06-24 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0015_event_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='title',
        ),
    ]