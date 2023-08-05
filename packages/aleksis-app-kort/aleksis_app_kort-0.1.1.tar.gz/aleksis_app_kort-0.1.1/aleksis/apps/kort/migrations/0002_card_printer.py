# Generated by Django 3.2.9 on 2021-11-30 20:07

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('kort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='print_finished_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Printed at'),
        ),
        migrations.AddField(
            model_name='card',
            name='print_started_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Printed at'),
        ),
        migrations.CreateModel(
            name='CardPrinter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_data', models.JSONField(default=dict, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('status', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline'), ('with_errors', 'With errors')], max_length=255, verbose_name='Status')),
                ('status_text', models.TextField(blank=True, verbose_name='Status text')),
                ('last_seen_at', models.DateTimeField(blank=True, null=True, verbose_name='Last seen at')),
                ('site', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'Card printer',
                'verbose_name_plural': 'Card printers',
            },
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='printed_with',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kort.cardprinter', verbose_name='Printed with'),
        ),
    ]
