# Generated by Django 5.0.6 on 2024-09-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_sitesettings_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
