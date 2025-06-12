from django.urls import path
from . import views

app_name = 'otherpages'

urlpatterns = [
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('', views.index_views, name='home'),
]