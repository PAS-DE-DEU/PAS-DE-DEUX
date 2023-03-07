from django.shortcuts import render
from Product.models import product

# Create your views here.

def home(request):
    prdts = product.objects.all().order_by('-id')
    context = {
        'prdts':prdts
    }
    return render(request, 'shop/home.html', context)

def shop(request):
    prdts = product.objects.all().order_by('-id')
    context = {
        'prdts':prdts
    }
    return render(request, 'shop/shop.html', context)

def detail(request, category_slug, product_slug):
    prdt = product.objects.get(slug=product_slug)
    relprdts = product.objects.filter(category=prdt.category).exclude(product_name=prdt)[:4]
    context = {
        'prdt':prdt,
        'relprdts':relprdts
    }
    return render(request, 'shop/detail.html', context)


# Settings
def settings(request):
    return render(request, 'shop/settings/MyOrders.html')

def AddAddress(request):
    return render(request, 'shop/settings/AddAddress.html')