# Generated by Django 5.0.6 on 2024-09-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_sitesettings_delete_backgroundtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='sub_title',
            field=models.CharField(default='sub_title', max_length=300),
        ),
    ]
