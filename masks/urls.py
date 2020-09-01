from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="index"),

    path('shop/', views.Shop.as_view(), name="shop"),
    path('about/', views.About.as_view(), name="about"),

]