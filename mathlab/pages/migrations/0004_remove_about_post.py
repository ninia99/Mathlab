# Generated by Django 5.0.6 on 2024-07-26 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_about_about_post_about_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='post',
        ),
    ]