# Generated by Django 5.1 on 2024-08-28 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0007_remove_mypost_username"),
    ]

    operations = [
        migrations.DeleteModel(
            name="mypost",
        ),
    ]
