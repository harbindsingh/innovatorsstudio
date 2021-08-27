# Generated by Django 2.2.14 on 2021-08-18 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eduPlatform', '0042_personaldevelopmentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDevelopmentCourseRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_given', models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=0)),
                ('review', models.TextField(blank=True, null=True)),
                ('mini_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduPlatform.MiniCourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]