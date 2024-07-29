from django.contrib import admin
from catalog.models import Product, Category


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
