from django.shortcuts import render, get_object_or_404, redirect
# messages
from django.contrib import messages
# Authentication
from django.contrib.auth.decorators import login_required
from App_Order.models import Cart, Order
from App_Shop.models import Product

# Create your views here.

@login_required 
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    # print("Item")
    # print(item)
    order_item = Cart.objects.get_or_create(user=request.user, item=item, purchased=False)
    # print("Order Item Object:")
    # print(order_item)
    # print(order_item[0])
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # print("Order Query Set")
    # print(order_qs)
    if order_qs.exists():
        order = order_qs[0] #converting order_qs to order
        # print("If Order exists")
        # print(order)
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This Item's Quantity is Updated")
            return redirect("App_Shop:home")
        else:
            order.order_items.add(order_item[0])
            messages.info(request, "This Item Was Added to your cart")
            return redirect("App_Shop:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request, "This Item was added to your cart")
        return redirect("App_Shop:home")
















