# Generated by Django 3.2.16 on 2023-01-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2', '0002_auto_20220822_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesstoken',
            name='device_id',
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='logged_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
