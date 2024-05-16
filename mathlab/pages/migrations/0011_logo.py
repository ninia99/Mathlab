# Generated by Django 5.0.4 on 2024-05-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_download_remove_about_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logo/')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logos',
            },
        ),
    ]
