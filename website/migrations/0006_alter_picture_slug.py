# Generated by Django 4.1 on 2023-02-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_picture_slug_alter_picture_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]