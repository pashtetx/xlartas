# Generated by Django 4.2.4 on 2024-02-22 03:47

import apps.filehost.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(default=apps.filehost.models.GenerateUploadKey, max_length=30)),
                ('size', models.IntegerField(blank=True, default=None, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_delete', models.DateTimeField(default=apps.filehost.models.NowPlus30Days)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to=apps.filehost.models.format_filehost_upload)),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('size', models.IntegerField(blank=True, default=None, null=True)),
                ('upload', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='filehost.upload')),
            ],
        ),
    ]
