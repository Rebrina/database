# Generated by Django 2.1.1 on 2019-08-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_remove_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=0, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]
