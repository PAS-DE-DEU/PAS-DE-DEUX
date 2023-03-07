from django.urls import path
from . import views
from Category.views import *
from Product.views import *

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('/login', views.AdminLogin, name='AdminLogin'),

    #User Management
    path('/Usermanagement', views.UserManagement, name='user_manage'),
    path('/user_status/<int:id>/<str:status>', views.user_status, name='user_status'),
    path('/deleteUser/<int:id>', views.deleteUser, name='deleteUser'),

    # Category
    path('/Category', category, name='category'),
    path('/AddCategory', Add_Category, name='Addcategory'),
    path('/EditCategory/<int:id>', Edit_category, name='EditCategory'),
    path('/Updatecategory/<int:id>', UpdateCategory, name='UpdateCategory'),
    path('/category_status/<int:id>/<str:status>', category_status, name='enable_category'),
    path('/deletecategory/<int:id>', DeleteCategory, name='deletecategory'), 

    # Product
    path('/products', Product, name='products'),
    path('/Addproduct', AddProduct, name='Addproduct'),
    path('/product_status/<int:id>/<str:status>', product_status, name='product_status'),
    path('/deleteproduct/<int:id>', deleteProduct, name='deleteproduct'),


    # Product
    path('/orders', views.Orders, name='orders'),

]