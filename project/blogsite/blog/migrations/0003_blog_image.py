# Generated by Django 5.0.6 on 2024-05-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='uploads/'),
        ),
    ]