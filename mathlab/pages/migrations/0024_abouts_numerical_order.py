# Generated by Django 5.0.6 on 2024-09-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_sitesettings_image_alter_sitesettings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouts',
            name='numerical_order',
            field=models.IntegerField(default=0),
        ),
    ]