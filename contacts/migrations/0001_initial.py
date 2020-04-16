# Generated by Django 3.0.4 on 2020-04-16 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.CharField(max_length=50)),
                ('car_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
