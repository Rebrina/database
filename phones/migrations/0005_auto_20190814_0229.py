# Generated by Django 2.1.1 on 2019-08-13 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20190814_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]