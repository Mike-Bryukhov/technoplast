from django.contrib import admin

from .models import Supplier, ProductType, ProductOrder  # Measure,


class OrderAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'product_quantity', 'product_type', 'order_datetime')
    search_fields = ('supplier_name', 'order_datetime')
    list_display_links = ('supplier_name', 'order_datetime')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'supplier_mobile', 'supplier_email')
    # list_display_links = ('supplier_name', 'supplier_email')
    search_fields = ('supplier_name',  'supplier_mobile', 'supplier_email')


admin.site.register(ProductOrder, OrderAdmin)  # , OrderAdmin
admin.site.register(Supplier)
admin.site.register(ProductType)
# admin.site.register(Measure)
