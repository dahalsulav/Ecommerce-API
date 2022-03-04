
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tomlkit import document

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include('APIapp.urls')),
    path('api/',include('djoser.urls')),
    path('api/',include('djoser.urls.authtoken')),
    path('api/',include('product.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
