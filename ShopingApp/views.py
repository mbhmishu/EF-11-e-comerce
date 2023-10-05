from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from ShopingApp.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class Home(ListView):
    model = Product
    template_name = 'shoppapp/home.html'



class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shoppapp/product_detail.html'