# Generated by Django 3.0.7 on 2020-06-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_blog_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pubDate',
        ),
    ]
