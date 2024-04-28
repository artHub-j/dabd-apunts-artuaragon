from django.contrib import admin

from .models import ProductTemplate, ProductVariant, ProductCategory

admin.site.register(ProductTemplate)
admin.site.register(ProductVariant)
admin.site.register(ProductCategory)