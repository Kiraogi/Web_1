# Generated by Django 5.0.3 on 2024-03-20 17:35

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_videofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание аудиофайла')),
                ('file', models.FileField(blank=True, null=True, upload_to='audio', verbose_name='Аудиофайл')),
            ],
            managers=[
                ('obj_audio', django.db.models.manager.Manager()),
            ],
        ),
    ]
