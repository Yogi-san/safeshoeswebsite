from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.basket_view, name='basket'),
    path('cart/', views.view_cart, name='view_cart')
]