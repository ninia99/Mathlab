# Generated by Django 5.0.6 on 2024-09-12 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_abouts_numerical_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abouts',
            name='numerical_order',
        ),
    ]