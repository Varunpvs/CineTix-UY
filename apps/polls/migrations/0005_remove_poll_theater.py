# Generated by Django 5.1.5 on 2025-03-16 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_poll_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='theater',
        ),
    ]
