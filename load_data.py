from django.core.management.base import BaseCommand
from products.models import Category, Product
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очищаем базу данных от старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Считываем данные из JSON-файла
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Создаем категории и продукты на основе данных из JSON
        categories = {}
        for item in data:
            if item['model'] == 'products.category':
                category = Category.objects.create(name=item['fields']['name'])
                categories[item['pk']] = category

        for item in data:
            if item['model'] == 'products.product':
                category_id = item['fields'].pop('category')
                category = categories[category_id]
                Product.objects.create(category=category, **item['fields'])

        self.stdout.write(self.style.SUCCESS('Database has been successfully filled.'))
