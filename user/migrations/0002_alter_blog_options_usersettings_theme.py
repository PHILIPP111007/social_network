# Generated by Django 4.2 on 2023-05-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date_time']},
        ),
        migrations.AddField(
            model_name='usersettings',
            name='theme',
            field=models.BooleanField(default=True),
        ),
    ]
