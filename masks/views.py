from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

# Create your views here.
class Home(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)

class Shop(View):
    template_name = 'shop.html'
    def get(self, request):
        return render(request, self.template_name)

class Cart(View):
    template_name = 'cart.html'
    def get(self, request):
        return render(request, self.template_name)

class CartAdd(View):
    template_name = 'cart.html'
    def post(self, request):
        item_des = request.POST['product_name']
        item = Item.create(item_des)
        return render(request, self.template_name, {item: "cart"})