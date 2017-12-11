# Generated by Django 2.0 on 2017-12-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0023_auto_20171121_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='ttl',
            field=models.PositiveIntegerField(default=60, help_text='Time to live; minutes until cached feed refreshed', null=True, verbose_name='TTL'),
        ),
    ]