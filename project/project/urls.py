from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', include('urlshortener.urls')),
    path('account/', include('app_login.urls')),
    path('', views.Index, name='Index'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)