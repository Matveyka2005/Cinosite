# Generated by Django 4.2 on 2023-04-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_film_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]