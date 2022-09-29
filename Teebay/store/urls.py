from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="store"),
    path('home', views.home, name="home"),
]