# Generated by Django 5.0.6 on 2024-09-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_alter_sitesettings_image_alter_sitesettings_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
