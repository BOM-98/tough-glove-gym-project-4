# Generated by Django 4.1 on 2023-11-17 18:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("layout", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comments",
            name="author",
        ),
        migrations.RemoveField(
            model_name="comments",
            name="post",
        ),
        migrations.DeleteModel(
            name="BlogPosts",
        ),
        migrations.DeleteModel(
            name="Comments",
        ),
    ]
