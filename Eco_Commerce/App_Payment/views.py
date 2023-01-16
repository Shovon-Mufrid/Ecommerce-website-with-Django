from django.shortcuts import render, HttpResponseRedirect, redirect
from App_Order.models import Order
from App_Payment.forms import BillingAddress
from App_Payment.forms import BillingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# for sslcommerz payment
import requests
# from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket

# Create your views here.

@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address) #form generate from Saved Address
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f"Shipping Address Saved")
    order_qs = Order.objects.filter(user=request.user, ordered = False)     
    orderItems = order_qs[0].order_items.all()
    order_total = order_qs[0].get_totals() #Order>model>get_totals
    return render(request, 'App_Payment/checkout.html', context={'form':form, "order_items": orderItems, "order_total": order_total, "saved_address": saved_address})



@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    if not saved_address[0].is_fully_filled():
        messages.info(request, f"Please complete shipping address!")
        return redirect("App_Payment:checkout")

    if not request.user.profile.is_fully_filled():
        messages.info(request, f"Complete Profile Details")
        return redirect("App_Login:profile")

    return render(request, "App_Payment/payment.html", context={})


