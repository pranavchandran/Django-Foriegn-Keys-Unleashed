# Generated by Django 3.0.7 on 2020-06-13 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0004_auto_20200613_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='passengers',
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
