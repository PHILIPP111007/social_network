# Generated by Django 4.1.5 on 2023-03-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_blog_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=models.TextField(max_length=5000),
        ),
    ]
