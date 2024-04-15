from django.db import migrations, models

def remove_manufactured_at(apps, schema_editor):
    Product = apps.get_model('catalog', 'Product')
    # Удаляем поле 'manufactured_at' из модели Product
    Product.objects.all().update(manufactured_at=None)  # Установите значения на None, если нужно

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        # Операция отката, удаляющая поле 'manufactured_at'
        migrations.RunPython(remove_manufactured_at),
    ]
