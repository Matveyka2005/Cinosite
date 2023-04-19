# Generated by Django 4.2 on 2023-04-19 09:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='viewers',
            field=models.ManyToManyField(related_name='films', through='films.UserFilmRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
