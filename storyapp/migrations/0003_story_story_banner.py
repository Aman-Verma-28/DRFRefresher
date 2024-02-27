# Generated by Django 4.0.4 on 2022-06-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_banner',
            field=models.ImageField(blank=True, default='images/defaults/story_banner.png', help_text='Banner image for the story (Ref: 1280x640px).', upload_to='images/story_banners/'),
        ),
    ]