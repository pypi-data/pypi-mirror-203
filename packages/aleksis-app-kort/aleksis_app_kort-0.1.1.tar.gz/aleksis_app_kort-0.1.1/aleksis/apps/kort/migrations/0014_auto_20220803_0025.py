# Generated by Django 3.2.14 on 2022-08-02 22:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kort', '0013_auto_20220530_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardlayout',
            options={'verbose_name': 'Card Layout', 'verbose_name_plural': 'Card Layouts'},
        ),
        migrations.AddField(
            model_name='cardlayout',
            name='required_fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=['first_name'], size=None, verbose_name='Required data fields'),
            preserve_default=False,
        ),
    ]
