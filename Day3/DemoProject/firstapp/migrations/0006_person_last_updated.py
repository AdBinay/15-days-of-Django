# Generated by Django 5.0.4 on 2024-04-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
