# Generated by Django 3.1.6 on 2021-02-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0014_auto_20210211_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_flag',
            field=models.ImageField(upload_to='country/country-flag-svg'),
        ),
    ]