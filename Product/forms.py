from django import forms
from django.forms import widgets
from .models import *

class AddProductForm(forms.ModelForm):
      class Meta:
        model = product
        fields = ["product_name","slug","description","image","category","Size","color","price","is_available"]
        widgets = {
        'product_name':forms.TextInput(attrs={'class':'text-light form-control'}),
        'slug':forms.TextInput(attrs={'class':'text-light form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'image': forms.FileInput(attrs={'class':'form-control'}),
        'category':forms.Select(attrs={'class':'text-light form-control'}),
        'Size':forms.Select(attrs={'class':'text-light form-control'}),
        'color': forms.TextInput(attrs={'class': 'selectpicker form-control', 'placeholder': 'color'}),
        'price': forms.NumberInput(attrs={'class':'text-light form-control active'}),
        'is_available':forms.CheckboxInput()
        }