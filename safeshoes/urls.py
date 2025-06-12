from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('', include('products.urls')),
    path('otherpages/', include('otherpages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)