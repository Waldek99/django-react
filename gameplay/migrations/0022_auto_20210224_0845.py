# Generated by Django 3.1.7 on 2021-02-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0021_auto_20210222_1159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SelectGameplay',
        ),
        migrations.AlterField(
            model_name='userselection',
            name='game_mode',
            field=models.CharField(choices=[('LE', 'League'), ('CU', 'Cup')], max_length=2),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='level_of_game',
            field=models.CharField(choices=[('IN', 'International'), ('CC', 'Club Competitions'), ('IC', 'International Club Competitions')], max_length=2),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='type_of_game',
            field=models.CharField(choices=[('FO', 'Football'), ('BA', 'Basketball'), ('HO', 'Hockey'), ('VO', 'Vollyball'), ('HA', 'Handball'), ('AF', 'American Football'), ('RF', 'Rugby Football'), ('SJ', 'Ski jumping')], max_length=2),
        ),
    ]
