# Generated by Django 4.0.5 on 2022-06-14 07:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_remove_profile_bio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Booking',
        ),
    ]
