from django.shortcuts import render
# Create your views here.
from App_Shop.models import Product 
# Import Views
from django.views.generic import ListView, DetailView

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'
    # by default context value is : object_list