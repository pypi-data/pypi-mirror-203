# Generated by Django 3.2.12 on 2022-03-10 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ('kort', '0005_card_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardprinter',
            name='oauth2_application',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.oauthapplication', verbose_name='OAuth2 application'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardprinter',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='cardprinter',
            name='status',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline'), ('with_errors', 'With errors'), ('not_registered', 'Not registered')], default='not_registered', max_length=255, verbose_name='Status'),
        ),
    ]
