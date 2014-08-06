from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'inventory_count', 'created']

admin.site.register(Product, ProductAdmin)