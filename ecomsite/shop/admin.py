from django.contrib import admin
from .models import Products, Order
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'discounted_price', 'category',)
    search_fields = ('title',)
    actions = (change_category_to_default,)
    fields = ('title', 'discounted_price')
    list_editable = ('discounted_price',)

admin.site.register(Products, ProductsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'city', 'state',)
    search_fields = ('name',)

admin.site.register(Order, OrderAdmin)

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "All About Shopping"
admin.site.index_title = "Manage Product"