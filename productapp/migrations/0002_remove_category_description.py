# Generated by Django 5.0.6 on 2024-06-03 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
