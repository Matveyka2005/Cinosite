# Generated by Django 4.2 on 2023-04-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_alter_film_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
