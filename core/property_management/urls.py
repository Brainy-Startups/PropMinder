
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('login_user/',views.login_user, name='login_user'),
    path('register_user/',views.register_user, name='register_user'),
    path('logout_user/',views.logout_user, name='logout_user'),
]
