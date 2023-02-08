# Generated by Django 4.1 on 2023-02-08 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phonnumber', models.BigIntegerField(null=True)),
                ('first_login', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]