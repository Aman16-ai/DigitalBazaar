# Generated by Django 4.1.5 on 2023-09-27 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 27, 14, 31, 54, 887855)),
        ),
    ]
