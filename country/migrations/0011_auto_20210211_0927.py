# Generated by Django 3.1.6 on 2021-02-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0010_auto_20210211_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_flag',
            field=models.ImageField(blank=True, null=True, upload_to='country/country-flag-svg/'),
        ),
    ]
