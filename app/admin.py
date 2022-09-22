from django.contrib import admin
from .models import (
    Customer, Product,
    Cart, OrderPlaced
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode']
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'description', 'brand', 'category', 'product_image']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','product', 'quantity']
@admin.register(OrderPlaced)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity','status']


