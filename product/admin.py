from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', "name", "price", "count")
    list_display_links = ('id', "name", "price", "count")
    prepopulated_fields = {"slug": ("name", "price", "count")}
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('name', 'id')
