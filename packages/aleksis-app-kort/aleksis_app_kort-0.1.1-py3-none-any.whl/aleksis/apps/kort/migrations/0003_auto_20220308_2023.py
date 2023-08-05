# Generated by Django 3.2.12 on 2022-03-08 19:23

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('kort', '0002_card_printer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='print_finished_at',
        ),
        migrations.RemoveField(
            model_name='card',
            name='print_started_at',
        ),
        migrations.RemoveField(
            model_name='card',
            name='printed_with',
        ),
        migrations.CreateModel(
            name='CardLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_data', models.JSONField(default=dict, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('template', models.TextField(verbose_name='Template')),
                ('css', models.TextField(blank=True, verbose_name='Custom CSS')),
                ('site', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
