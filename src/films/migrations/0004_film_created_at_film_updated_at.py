# Generated by Django 4.2 on 2023-04-19 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_userfilmrelation_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
