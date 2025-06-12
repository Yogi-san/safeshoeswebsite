from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, ProductReview
from django.contrib import messages
from django.urls import reverse
from .forms import ReviewForm
from django.http import JsonResponse


def index_view(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


@login_required
def favorites_view(request):
    favorites = request.user.favorites.all()
    return render(request, 'products/favorites.html', {'favorites': favorites})


@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    if product in user.favorites.all():
        user.favorites.remove(product)
        is_favorite = False
    else:
        user.favorites.add(product)
        is_favorite = True

    # اگر درخواست AJAX باشد (از JS ارسال شده):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'is_favorite': is_favorite})
    # اگر از طریق فرم ارسال شده:
    return redirect('products:index')


def rate_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.user.is_authenticated:
        messages.info(request, 'برای امتیازدهی باید وارد حساب کاربری خود شوید')
        return redirect(f'{reverse("accounts:login")}?next={request.path}')

    try:
        user_review = ProductReview.objects.get(product=product, user=request.user)
        edit_mode = True
    except ProductReview.DoesNotExist:
        user_review = None
        edit_mode = False

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=user_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد')
            return redirect('products:index')
    else:
        form = ReviewForm(instance=user_review)

    return render(request, 'products/rate_product.html', {
        'form': form,
        'product': product,
        'edit_mode': edit_mode
    })


def home(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})