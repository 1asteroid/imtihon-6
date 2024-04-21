from django.contrib import admin
from .models import Basket, BasketItems
from import_export.admin import ImportExportModelAdmin


@admin.register(Basket)
class BasketAdmin(ImportExportModelAdmin):
    list_display = ("id", "user", "create_date")
    list_display_link = ("id", "user", "create_date")
    search_fields = ("id", "user")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', )


@admin.register(BasketItems)
class BasketItemsAdmin(ImportExportModelAdmin):
    list_display = ("id", "basket", "product", "quantity")
    list_display_links = ("id", "basket", "product", "quantity")
    prepopulated_fields = {"slug": ("product", "quantity",)}
    search_fields = ("id", "product")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('basket', 'id')

