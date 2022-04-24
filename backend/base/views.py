from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from base.models import Product
from .ressource.products import products

# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'hello.html',{})


class ProductList(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'listProducts.html',{'products':products})
