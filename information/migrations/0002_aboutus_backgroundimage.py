# Generated by Django 5.0.4 on 2024-04-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='backgroundImage',
            field=models.ImageField(blank=True, null=True, upload_to='bg_logo/'),
        ),
    ]
