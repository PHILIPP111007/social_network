# Generated by Django 4.2 on 2023-04-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_room_user_1_alter_room_user_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='delete_number',
            field=models.SmallIntegerField(default=0),
        ),
    ]
