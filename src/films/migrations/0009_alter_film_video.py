# Generated by Django 4.2 on 2023-04-21 08:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_film_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
