from django.urls import path
from urlshortener import views
from .views import home_view, redirect_url_view

appname = "urlshortener"

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('<str:signup/', views.sign_up, name='signup'),


]
