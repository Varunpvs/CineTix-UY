# Generated by Django 5.1.5 on 2025-03-10 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='theater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theaters.theater'),
        ),
    ]
