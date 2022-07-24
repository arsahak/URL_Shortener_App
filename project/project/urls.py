from django.contrib import admin
from django.urls import path, include
from urlshortener import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlshortener.urls')),
]
