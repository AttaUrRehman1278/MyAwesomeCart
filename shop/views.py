from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    product_data = Product.objects.all()
    context = {
        'product_data':product_data
    }
    return render(request , 'shop/index.html', context)

def about(request):
    return HttpResponse("This is about")

def contact(request):
    return HttpResponse("This is contact us")

def tracker(request):
    return HttpResponse("This is Tracking Status")

def search(request):
    return HttpResponse("This is search")

def productview(request):
    return HttpResponse("This is product view")

def checkout(request):
    return HttpResponse("This is checkout")
