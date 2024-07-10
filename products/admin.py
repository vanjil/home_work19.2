from django.contrib import admin
from .models import Category, Product, Version  # Используйте только один раз модуль models

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'year')
    list_filter = ('category', 'year')
    search_fields = ('name', 'year')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_name', 'version_number', 'is_current')
    list_filter = ('product', 'is_current')
    search_fields = ('version_name', 'version_number')
