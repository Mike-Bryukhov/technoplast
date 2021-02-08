from django.contrib import admin

from .models import Supplier, ProductType, Measure, ProductOrder


admin.site.register(Supplier)
admin.site.register(ProductType)
admin.site.register(Measure)
admin.site.register(ProductOrder)
