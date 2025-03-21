# Generated by Django 5.1.5 on 2025-03-08 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yes_votes', models.PositiveIntegerField(default=0)),
                ('threshold', models.PositiveIntegerField(default=50, help_text='Minimum votes required to approve movie')),
                ('decision', models.BooleanField(blank=True, default=None, help_text='True if movie will be released', null=True)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
