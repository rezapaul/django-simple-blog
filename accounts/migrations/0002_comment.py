# Generated by Django 3.0.8 on 2020-07-10 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('user_photo', models.CharField(default='http://127.0.0.1:8000/media/users_photo/author.png', max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
