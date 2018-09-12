from django.contrib import admin
from .models import Product,Order, MiddleMan, Category

# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(MiddleMan)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'img')
admin.site.register(Product, ProductAdmin)

class MiddleManInline(admin.TabularInline):
    model = MiddleMan


class OrderAdmin(admin.ModelAdmin):
#    list_display = (['user', 'date_of_purchase'])
    inlines = [
        MiddleManInline,
    ]
admin.site.register(Order, OrderAdmin)



admin.site.register(MiddleMan)
admin.site.register(Category)
