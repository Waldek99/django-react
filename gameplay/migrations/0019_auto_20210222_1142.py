# Generated by Django 3.1.7 on 2021-02-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0018_auto_20210222_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectgameplay',
            name='game_mode_description',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='game_mode_description',
        ),
        migrations.AlterField(
            model_name='selectgameplay',
            name='type_of_game',
            field=models.CharField(max_length=120),
        ),
    ]