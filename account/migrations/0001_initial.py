# Generated by Django 4.0.5 on 2022-08-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_no', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
            ],
        ),
    ]
