from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Category
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages

# Create your views here.

@never_cache
@staff_member_required(login_url='AdminLogin')
def category(request):
    if 'key' in request.GET:
        key = request.GET.get('key')
        if key:
            ctgy = Category.objects.filter(category_name__icontains = key).order_by('-id')
        else:
            return redirect('category')
    else:
        ctgy = Category.objects.all().order_by('-id')
    ctgycount = ctgy.count()
    paginator = Paginator(ctgy, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        "ctgy":paged_products,
        "ctgycount":ctgycount,
    }
    return render(request, 'Backend/Category/category.html', context)

@never_cache
@staff_member_required(login_url='adminlogin')
def Add_Category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST , request.FILES)
        if form.is_valid():
            form.errors.as_data()
            form.save()
            return redirect('category')
        else:
            messages.error(request, 'Category name Already exist')
            return redirect('Addcategory')
    else:
        form = AddCategoryForm()
    context={
        "form":form 
    }
    return render(request, 'Backend/Category/AddCategory.html', context)

@never_cache
@staff_member_required(login_url='AdminLogin')
def Edit_category(request, id):
    ctgy = Category.objects.get(id=id)
    context = {
        'ctgy':ctgy
    }
    return render(request, 'Backend/Category/EditCategory.html', context)

@never_cache
@staff_member_required(login_url='adminlogin')
def UpdateCategory(request,id):
    ctgy = Category.objects.get(id=id)
    form = EditCategoryForm(request.POST, instance = ctgy)
    if form.is_valid():  
        form.save()  
        return redirect("category")
    else:
         messages.error(request, 'Category name already exist')
    context = {
        'ctgy': ctgy
    }  
    return render(request, 'Backend/Category/EditCategory.html', context)

@never_cache
@staff_member_required(login_url='adminlogin')
def category_status(request,id,status):
    ctgy = Category.objects.get(id=id)
    if status == 'true':  
        print('true')
        ctgy.is_active = True
    elif status == 'false':
        print('fal')
        ctgy.is_active = False
    ctgy.save()
    return redirect('category') 

@never_cache
@staff_member_required(login_url='adminlogin')
def DeleteCategory(request, id):
    ctgy = Category.objects.filter(id=id)
    ctgy.delete()
    return redirect('category')