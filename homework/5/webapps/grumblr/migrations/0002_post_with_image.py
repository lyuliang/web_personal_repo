# Generated by Django 2.1.1 on 2018-10-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='with_image',
            field=models.BooleanField(default=False),
        ),
    ]