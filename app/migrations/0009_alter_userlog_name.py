# Generated by Django 4.1.3 on 2022-11-17 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_delete_man'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='name',
            field=models.OneToOneField(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
