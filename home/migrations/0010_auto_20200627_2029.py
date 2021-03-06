# Generated by Django 3.0.7 on 2020-06-27 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200627_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_on']},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='published',
        ),
        migrations.AddField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
