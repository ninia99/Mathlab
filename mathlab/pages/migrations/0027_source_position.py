# Generated by Django 5.0.6 on 2024-09-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_abouts_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='position',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
