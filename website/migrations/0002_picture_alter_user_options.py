# Generated by Django 4.1 on 2023-02-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('img', models.ImageField(height_field=400, upload_to='', width_field=400)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'picture',
                'verbose_name_plural': 'pictures',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-first_login'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
