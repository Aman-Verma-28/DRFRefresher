# Generated by Django 4.0.4 on 2022-06-11 09:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(help_text='Title of the story.', max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, help_text='Short summary of the story.', max_length=1000, null=True)),
                ('body', models.TextField()),
                ('genre', models.CharField(blank=True, choices=[('comedy', 'Comedy'), ('drama', 'Drama'), ('fable', 'Fable'), ('fairy Tale', 'Fairy Tale'), ('fantasy', 'Fantasy'), ('folklore', 'Folklore'), ('historical_fiction', 'Historical Fiction'), ('horror', 'Horror'), ('legend', 'Legend'), ('mystery', 'Mystery'), ('mythology', 'Mythology'), ('parody', 'Parody'), ('romance', 'Romance'), ('saga', 'Saga'), ('science_fiction', 'Science Fiction')], max_length=32, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
                'ordering': ('-created_at',),
            },
        ),
    ]
