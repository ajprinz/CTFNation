# Generated by Django 2.2.11 on 2020-03-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200212_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]