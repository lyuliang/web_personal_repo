# Generated by Django 2.1.1 on 2018-10-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default='there is hope', max_length=128),
        ),
    ]
