# Generated by Django 5.0.6 on 2024-09-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_merge_20240814_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('title', models.CharField(null=True)),
            ],
            options={
                'verbose_name': 'source',
                'verbose_name_plural': 'sources',
            },
        ),
    ]
