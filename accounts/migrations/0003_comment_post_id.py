# Generated by Django 3.0.8 on 2020-07-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
    ]
