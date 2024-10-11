from django.contrib import admin
from .models import Category, Announcement, Version  # Убедитесь, что здесь Announcement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'owner', 'published')
    list_filter = ('category', 'owner', 'published')
    search_fields = ('title',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement', 'version_name', 'version_number', 'is_current')
    list_filter = ('announcement', 'is_current')
    search_fields = ('version_name', 'version_number')
