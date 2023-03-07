from django.shortcuts import render

# Create your views here.


def Cart(request):
    return render(request, 'shop/cart.html')

def  Checkout(request):
    return render(request, 'shop/checkout.html')