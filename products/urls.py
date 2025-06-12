from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('product/<int:product_id>/rate/', views.rate_product, name='rate_product'),
    path('product/<int:product_id>', views.product_detail, name='product_detail')
]