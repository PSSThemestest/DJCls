# Generated by Django 2.0.7 on 2018-07-11 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
