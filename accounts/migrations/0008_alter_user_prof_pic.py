# Generated by Django 4.1 on 2023-02-14 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_special_til'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prof_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profpics/'),
        ),
    ]
