# Generated by Django 2.0.7 on 2018-07-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
