from django.shortcuts import render
# Create your views here.
from App_Shop.models import Product 
# Import Views
from django.views.generic import ListView, DetailView
#mixin
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'
    # by default context value is : object_list


class ProductDetail(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'App_Shop/product_details.html'  
        # by default context value is : object
