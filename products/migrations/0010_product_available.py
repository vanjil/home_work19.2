# Generated by Django 5.0.3 on 2024-05-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_blogpost_slug_alter_product_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
