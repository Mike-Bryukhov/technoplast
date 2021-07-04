from django.contrib import admin

from .models import ProductType, ProductOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_name', 'supplier_mobile', 'supplier_email',
                    'product_quantity', 'product_type', 'order_datetime')
    search_fields = ('supplier_name', 'supplier_mobile', 'supplier_email',
                     'order_datetime')
    list_display_links = ('supplier_name', 'supplier_mobile', 'supplier_email', 'order_datetime')


admin.site.register(ProductOrder, OrderAdmin)
admin.site.register(ProductType)
