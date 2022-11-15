from django.contrib import admin
from .models import Products, ProductMaster, StorMaster


# Register your models here.


class ProductsClass(admin.ModelAdmin):
    list_display = ['item_name', 'unit', 'price']


class StorMasterClass(admin.ModelAdmin):
    list_display = ['product', 'stor_master_name', 'location']


class ProductMasterClass(admin.ModelAdmin):
    list_display = ['product', 'product_master_name', 'manufacturer', 'price']


admin.site.register(Products, ProductsClass)
admin.site.register(StorMaster, StorMasterClass)
admin.site.register(ProductMaster, ProductMasterClass)
