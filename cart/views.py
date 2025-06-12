from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.http import JsonResponse
from .models import Cart, CartItem


@login_required
def basket_view(request):
    context = {
        'items': request.session.get('cart_items', []),
        'total': sum(item['price'] for item in request.session.get('cart_items', []))
    }
    return render(request, 'cart/basket.html', context)


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)
        size = request.POST.get('size')
        color = request.POST.get('color')

        # ایجاد یا دریافت سبد خرید کاربر
        cart, _ = Cart.objects.get_or_create(user=request.user)

        # افزودن محصول به سبد
        product = get_object_or_404(Product, id=product_id)
        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
            size=size,
            color=color
        )
        return JsonResponse({
            'status': 'success',
            'message': 'محصول به سبد اضافه شد!',
            'cart_items_count': cart.items.count()
        })

    return JsonResponse({'status': 'error'})


@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})