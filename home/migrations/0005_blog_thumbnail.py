# Generated by Django 3.0.6 on 2020-06-26 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
