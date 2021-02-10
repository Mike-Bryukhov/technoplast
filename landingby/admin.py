from django.contrib import admin

from .models import Supplier, ProductType, ProductOrder  # Measure,


admin.site.register(Supplier)
admin.site.register(ProductType)
# admin.site.register(Measure)
admin.site.register(ProductOrder)
