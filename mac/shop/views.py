from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    product_list = Product.objects.all()
    print(product_list)
    return render(request, 'shop/index.html', {'product_list': product_list})


def about(request):
    return HttpResponse('this is about page')


def contact(request):
    return HttpResponse('this is contact page')


def tracker(request):
    return HttpResponse('this is tracker page')


def search(request):
    return HttpResponse('this is search page')


def productView(request):
    return HttpResponse('this is productView page')


def checkout(request):
    return HttpResponse('this is checkout page')
