# Generated by Django 3.0.5 on 2020-07-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=36)),
            ],
        ),
    ]
