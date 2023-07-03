from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Transaction)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('product_id',)  # Make the product ID field read-only

admin.site.register(Product, ProductAdmin)