# Generated by Django 4.1 on 2023-02-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_prof_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prof_pic',
            field=models.ImageField(default='../static/img/defult_prof.jpg', upload_to='profpics/'),
        ),
    ]