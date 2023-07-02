from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    pass
class UnderCategoryAdmin(admin.ModelAdmin):
    pass
class BrandAdmin(admin.ModelAdmin):
    pass
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin),
admin.site.register(UnderCategory, UnderCategoryAdmin),
admin.site.register(Brand, BrandAdmin),
admin.site.register(Product, ProductAdmin)