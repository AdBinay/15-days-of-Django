# Generated by Django 5.0.4 on 2024-04-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
