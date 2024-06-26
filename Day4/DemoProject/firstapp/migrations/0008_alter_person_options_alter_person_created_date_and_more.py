# Generated by Django 5.0.4 on 2024-04-29 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_person_profile_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Peoples', 'verbose_name_plural': 'people'},
        ),
        migrations.AlterField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='user created'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('bio', models.TextField(max_length=500)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstapp.person')),
            ],
        ),
    ]
