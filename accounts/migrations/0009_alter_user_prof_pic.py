# Generated by Django 4.1 on 2023-02-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_prof_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prof_pic',
            field=models.ImageField(blank=True, default='static/img/30089800.jpg', null=True, upload_to='profpics/'),
        ),
    ]
