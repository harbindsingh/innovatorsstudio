# Generated by Django 2.2.14 on 2021-08-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0032_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='Unknown', max_length=30),
        ),
    ]
