# Generated by Django 3.1.7 on 2021-03-03 14:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameplay', '0026_auto_20210303_1307'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSelection',
            new_name='GameplaySelection',
        ),
    ]
