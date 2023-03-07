from django.urls import path
from . import views

urlpatterns=[
    path('', views.UserLogin, name='UserLogin'),
    path('sign-up/', views.Register, name='register'),
    path('log-out/', views.UserLogout, name='UserLogout'),
]