# Generated by Django 5.1.4 on 2024-12-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
