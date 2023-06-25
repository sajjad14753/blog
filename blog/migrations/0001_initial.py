# Generated by Django 4.2.2 on 2023-06-09 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
