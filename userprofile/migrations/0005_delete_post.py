# Generated by Django 5.1 on 2024-08-27 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0004_remove_post_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Post",
        ),
    ]
