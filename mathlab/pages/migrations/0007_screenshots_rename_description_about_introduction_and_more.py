# Generated by Django 5.0.4 on 2024-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_demo_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
            ],
            options={
                'verbose_name': 'screenshot',
                'verbose_name_plural': 'screenshots',
            },
        ),
        migrations.RenameField(
            model_name='about',
            old_name='description',
            new_name='introduction',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image',
        ),
        migrations.AddField(
            model_name='about',
            name='license',
            field=models.TextField(blank=True, null=True),
        ),
    ]