from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    params = {'no_of_slides':nSlides,'range':range(1, nSlides),'product': products}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
def product(request):
    product_data = Product.objects.all()
    context = {
        'product_data':product_data
    }
    return render(request , 'shop/product.html', context)

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
