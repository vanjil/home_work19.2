# Generated by Django 5.0.6 on 2024-05-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_version_version_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_name',
            field=models.CharField(max_length=255),
        ),
    ]
