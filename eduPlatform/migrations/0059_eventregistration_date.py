# Generated by Django 2.2.14 on 2021-08-25 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0058_eventregistration_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
