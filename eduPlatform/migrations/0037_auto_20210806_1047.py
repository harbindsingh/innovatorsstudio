# Generated by Django 2.2.14 on 2021-08-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0036_auto_20210806_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc2',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc3',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc4',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc5',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
