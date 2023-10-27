from django.contrib import admin
from django.urls import path
from .views import *
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('registration', user_views.registration, name = 'Registration'),
    path('login/', auth_views.LoginView.as_view(template_name = 'store/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'store/logout.html'), name = 'logout'),
    path('product_detail/<pk>', product_details, name = 'product_detail'),
    path('add_to_cart/<pk>', add_to_cart, name = 'add_to_cart'),
    path('remove_from_cart/<pk>', remove_from_cart, name = 'remove_from_cart'),

    path('show/', show, name = 'scrape'),
    path('add_scrape/', add, name='add_scrape'),
] 