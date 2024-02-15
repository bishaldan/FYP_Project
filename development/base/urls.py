from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('login.html', views.login_page, name='login_page_html'),
]
