# Generated by Django 4.1 on 2023-02-10 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_picture_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
