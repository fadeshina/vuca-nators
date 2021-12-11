# Generated by Django 3.2.9 on 2021-12-06 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211205_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwatchlist',
            name='watched_list',
        ),
        migrations.AddField(
            model_name='userwatchlist',
            name='watchlist',
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name='userwatchlist',
            name='user',
        ),
        migrations.AddField(
            model_name='userwatchlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]