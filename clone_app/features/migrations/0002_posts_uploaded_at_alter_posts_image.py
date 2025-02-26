# Generated by Django 5.0.6 on 2025-02-18 12:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
