# Generated by Django 3.0.7 on 2020-06-13 21:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_auto_20200613_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='first_owner',
        ),
        migrations.AddField(
            model_name='car',
            name='passengers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
