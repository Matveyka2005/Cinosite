# Generated by Django 4.2 on 2023-04-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_film_created_at_film_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmdata',
            name='name',
            field=models.CharField(default='Form of voice', max_length=200),
            preserve_default=False,
        ),
    ]
