from django.shortcuts import render, HttpResponseRedirect
from App_Order.models import Order
from App_Payment.forms import BillingAddress
from App_Payment.forms import BillingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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








