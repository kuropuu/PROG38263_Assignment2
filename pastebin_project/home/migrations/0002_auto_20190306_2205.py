# Generated by Django 2.1.7 on 2019-03-06 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='expiry',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='paste',
            name='invited_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paste',
            name='privacy',
            field=models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=10),
        ),
        migrations.AddField(
            model_name='paste',
            name='status',
            field=models.CharField(choices=[('Enabled', 'Enabled'), ('Disabled', 'Disabled')], default='Enabled', max_length=10),
        ),
        migrations.AlterField(
            model_name='paste',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paste_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
