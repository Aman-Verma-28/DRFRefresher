# Generated by Django 4.0.4 on 2022-06-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrymodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
