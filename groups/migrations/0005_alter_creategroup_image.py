# Generated by Django 5.1 on 2024-08-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_alter_creategroup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creategroup',
            name='image',
            field=models.ImageField(blank=True, upload_to='media\\groups'),
        ),
    ]
