# Generated by Django 5.0.6 on 2024-08-01 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_about_post_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
