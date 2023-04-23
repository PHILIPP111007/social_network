# Generated by Django 4.2 on 2023-04-23 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('user_1', models.CharField(max_length=500)),
                ('user_2', models.CharField(max_length=500)),
                ('delete_user_1', models.CharField(default='0', max_length=500)),
                ('delete_user_2', models.CharField(default='0', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('room_name', models.ForeignKey(db_column='room_name', on_delete=django.db.models.deletion.CASCADE, to='chat.room')),
                ('sender', models.ForeignKey(db_column='sender', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
