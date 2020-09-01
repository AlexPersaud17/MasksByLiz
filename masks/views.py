from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Product, Cart, Order
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


class Shop(ListView):
    model = Product
    template_name = 'shop.html'


class Home(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)

class About(View):
    template_name = 'about.html'
    def get(self, request):
        return render(request, self.template_name)



class MaskDetail(View):
    template_name = 'mask-detail.html'
    def get(self, request, pk):
        mask = Product.objects.get(pk=pk)
        return render(request, self.template_name, {"mask": mask})


# def add_to_cart(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     order_item, created = Cart.objects.get_or_create(
#         item=item,
#         user=request.user
#     )

#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.orderitems.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.success(request, "This item quantity was updated.")
#             return redirect("shop")
#         else:
#             order.orderitems.add(order_item)
#             messages.success(request, "This item was added to your cart.")
#             return redirect("shop")
#     else:
#         order = Order.objects.create(user=request.user)
#         order.orderitems.add(order_item)
#         messages.success(request, "This item was added to your cart.")
#         return redirect("shop")

# def remove_from_cart(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     cart_qs = Cart.objects.filter(user=request.user, item=item)
#     if cart_qs.exists():
#         cart = cart_qs[0]
#         # Checking the cart quantity
#         if cart.quantity > 1:
#             cart.quantity -= 1
#             cart.save()
#         else:
#             cart_qs.delete()
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.orderitems.filter(item__slug=item.slug).exists():
#             order_item = Cart.objects.filter(
#                 item=item,
#                 user=request.user,
#             )[0]
#             order.orderitems.remove(order_item)
#             messages.success(request, "This item was removed from your cart.")
#             return redirect("shop")
#         else:
#             messages.success(request, "This item was not in your cart")
#             return redirect("shop")
#     else:
#         messages.success(request, "You do not have an active order")
#         return redirect("shop")


# def CartView(request):

#     user = request.user

#     carts = Cart.objects.filter(user=user)
#     orders = Order.objects.filter(user=user, ordered=False)
#     if carts.exists():
#         order = orders[0]
#         return render(request, 'cart.html', {"carts": carts, 'order': order})
		
#     else:
#         messages.warning(request, "You do not have an active order")
#         return redirect("shop")


# def decreaseCart(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.orderitems.filter(item__slug=item.slug).exists():
#             order_item = Cart.objects.filter(
#                 item=item,
#                 user=request.user
#             )[0]
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#                 order_item.save()
#             else:
#                 order.orderitems.remove(order_item)
#                 order_item.delete()
#             messages.info(request, f"{item.name} quantity has updated.")
#             return redirect("cart")
#         else:
#             messages.info(request, f"{item.name} quantity has updated.")
#             return redirect("cart")
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("cart")

        