# Generated by Django 3.1.7 on 2021-02-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0017_selectgameplay_userselection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectgameplay',
            name='type_of_game',
            field=models.CharField(choices=[('FO', 'Football'), ('BA', 'Basketball'), ('HO', 'Hockey'), ('VO', 'Vollyball'), ('HA', 'Handball'), ('AF', 'American Football'), ('RF', 'Rugby Football'), ('SJ', 'Ski jumping')], max_length=2),
        ),
    ]
