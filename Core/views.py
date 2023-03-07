from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from Accounts.models import Account


# Create your views here.

def AdminLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_superadmin:
                login(request, user)
                return redirect('Dashboard')
            else:
                messages.info(request, 'Permission Dinied')
                return redirect('AdminLogin')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('AdminLogin')
    else:
        return render(request, 'Backend/login.html')

@never_cache
@staff_member_required(login_url='AdminLogin')
def Dashboard(request):
    print('helo')
    return render(request, 'Backend/Dashboard.html')

# Users
@never_cache
@staff_member_required(login_url='AdminLogin')
def UserManagement(request):
    if 'key' in request.GET:
        key = request.GET.get('key')
        if key:
            users = Account.objects.filter(email__icontains = key, is_superadmin = False)
        else:
            return redirect('Users')
    else:
        users = Account.objects.filter(is_superadmin = False).order_by('-id')
    usercount = users.count()
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'users':paged_products,
        'usercount':usercount
    }
    return render(request, 'Backend/Usermanagement.html', context)

@never_cache
@staff_member_required(login_url='AdminLogin')
def user_status(request,id,status):
    users = Account.objects.get(id=id)
    if status == 'true':  
        users.is_active = True
    elif status == 'false':
        users.is_active = False
    users.save()
    return redirect('user_manage')

@never_cache
@staff_member_required(login_url='AdminLogin')
def deleteUser(request,id):
    users = Account.objects.get(id=id)
    users.delete()
    messages.error(request, 'User deleted Successfully')
    return redirect('user_manage')


# Orders
@never_cache
@staff_member_required(login_url='AdminLogin')
def Orders(request):
    return render(request, 'Backend/Order/orders.html')




# Offers
