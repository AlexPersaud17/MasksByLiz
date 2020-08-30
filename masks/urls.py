from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="index"),

    path('shop/', views.Shop.as_view(), name="shop"),
    path('about/', views.About.as_view(), name="about"),
    path('cart/', views.CartView, name="cart"),

    path('<int:pk>/', views.MaskDetail.as_view(), name="mask-detail"),
    path('cart/<slug>', views.add_to_cart, name='add-cart'),
    path('remove/<slug>', views.remove_from_cart, name='remove-cart'),
]