from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login-user/', views.loginhand,name='login'),
    path('logout-user/', views.logouthand,name='logout'),
    path('signup-user/', views.signuphand,name='Create account'),
]