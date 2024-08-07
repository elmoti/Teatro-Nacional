from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('utileria.urls')),
    path('admin/', admin.site.urls),
    path('', include('login_signup.urls')),
    path('', include('cartelera.urls')),
    path('', include('eventos.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)