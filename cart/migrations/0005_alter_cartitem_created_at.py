# Generated by Django 4.1.1 on 2022-09-08 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartitem_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 20, 35, 15, 897465)),
        ),
    ]
