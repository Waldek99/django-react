# Generated by Django 3.1.5 on 2021-02-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0008_auto_20210211_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_flag',
            field=models.ImageField(blank=True, null=True, upload_to='country/country-flag'),
        ),
    ]