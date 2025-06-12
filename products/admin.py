from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Product, ProductSize, ProductColor, ProductReview, Order, OrderItem


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ['created_at', 'status']
    can_delete = False

    def has_add_permission(self, request, obj):
        return False


class CustomUserAdmin(UserAdmin):
    inlines = [OrderInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'order_count')

    def order_count(self, obj):
        return obj.order_set.count()

    order_count.short_description = 'Orders'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'size', 'color', 'quantity', 'price']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'user', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('productname', 'userusername')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline, ProductColorInline]
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)