# Generated by Django 4.1.5 on 2023-05-12 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_cartitem_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 21, 12, 21, 403104)),
        ),
    ]
