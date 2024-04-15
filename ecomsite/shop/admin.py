from django.contrib import admin
from .models import Products, Order
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'discounted_price', 'category')

admin.site.register(Products, ProductsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_order = ('name', 'email', 'address', 'city', 'state')

admin.site.register(Order, OrderAdmin)