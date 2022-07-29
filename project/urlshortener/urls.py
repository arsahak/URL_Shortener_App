from django.urls import path
from urlshortener import views
from .views import home_view, redirect_url_view

appname = "urlshortener"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('test', views.test, name='test' ),
    path('urlchange/', views.custom_url, name='urlchange'),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect'),
]
