# Generated by Django 2.2.11 on 2020-03-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200310_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='kdratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wlratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
