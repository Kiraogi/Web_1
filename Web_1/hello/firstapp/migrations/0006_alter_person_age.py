# Generated by Django 5.0.3 on 2024-03-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_alter_person_age_alter_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='Возраст клиента'),
        ),
    ]
