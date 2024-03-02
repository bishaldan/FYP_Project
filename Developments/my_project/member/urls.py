from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashoard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name="loginpage"),
    path('logout/', auth_views.LoginView.as_view(), name="logout"),
]
