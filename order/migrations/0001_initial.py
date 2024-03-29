# Generated by Django 4.1.5 on 2023-05-12 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_address'),
        ('cart', '0010_alter_cartitem_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('PROCESSING', 'PROCESSING'), ('SHIPPED', 'SHIPPED'), ('DELIVERED', 'DELIVERED')], default='PENDING', max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_address', to='account.address')),
                ('items', models.ManyToManyField(to='cart.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to='account.userprofile')),
            ],
        ),
    ]
