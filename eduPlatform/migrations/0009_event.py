# Generated by Django 3.1.7 on 2021-05-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0008_auto_20210501_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('person_by', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('link', models.CharField(max_length=800)),
                ('registrationForm_link', models.CharField(max_length=800)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]