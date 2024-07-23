from django.core.cache import cache

from config.settings import CACHE_ENABLED
from products.models import Product

def get_product_from_cache():
    """ Получаем данные о продукте из кэша, если кэш пуст, получим продукт из б.д."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
