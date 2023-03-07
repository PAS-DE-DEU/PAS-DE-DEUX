from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Category
from django.core.paginator import Paginator
from .models import product
from .forms import *
from django.contrib import messages
# Create your views here.


@never_cache
@staff_member_required(login_url='AdminLogin')
def Product(request):
    if 'key' in request.GET:
        key = request.GET.get('key')
        if key:
            prdts = product.objects.filter(product_name__icontains = key).order_by('-id')
        else:
            return redirect('subproduct')
    else:
        prdts = product.objects.all().order_by('-id')
    pdt = prdts.count()
    paginator = Paginator(prdts, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'prdts':paged_products,
        'pdt':pdt,
    }
    return render(request, 'Backend/Product/products.html', context)

@never_cache
@staff_member_required(login_url='adminlogin')
def AddProduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            messages.info(request, 'Product already Added')
            return redirect('Addproduct')
    else:
        form = AddProductForm()
    context = {
        'form': form,
        }
    return render(request, 'Backend/Product/AddProduct.html', context)

@never_cache
@staff_member_required(login_url='adminlogin')
def product_status(request,id,status):
    prdts = product.objects.get(id=id)
    if status == 'true':  
        prdts.is_available = True
    elif status == 'false':
        prdts.is_available = False
    prdts.save()
    return redirect('products')

@never_cache
@staff_member_required(login_url='adminlogin')
def deleteProduct(request, id):
    prdt = product.objects.filter(id=id)
    prdt.delete()
    return redirect('products')