# Generated by Django 3.1.5 on 2021-02-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0005_auto_20210209_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=120)),
                ('nick_name', models.CharField(blank=True, max_length=300, null=True)),
                ('description_name', models.TextField(blank=True, null=True)),
                ('country_code2', models.CharField(blank=True, max_length=2, null=True)),
                ('country_code3', models.CharField(blank=True, max_length=3, null=True)),
                ('country_flag', models.ImageField(blank=True, null=True, upload_to='country-flag')),
                ('timestamps', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]