from django.contrib import admin
from catalog.models import Product, Category, Contacts, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')
    list_filter = ('name',)
    search_fields = ('name', 'phone',)


@admin.register(Version)
class VersionProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'num_vers', 'is_current_vers')
    list_filter = ('product', 'is_current_vers',)
    search_fields = ('name', 'product')
