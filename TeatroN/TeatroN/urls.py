from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('utileria.urls')),
    path('admin/', admin.site.urls),
    path('login_signup/', include('login_signup.urls')),
    path('', include('login_signup.urls')),
]
