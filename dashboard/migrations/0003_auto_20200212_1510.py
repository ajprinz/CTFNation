# Generated by Django 2.2.6 on 2020-02-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200212_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='losses',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='wins',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
