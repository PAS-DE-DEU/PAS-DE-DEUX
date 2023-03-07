from django import forms
from .models import *
from django.forms import widgets

class AddCategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ["category_name","slug","Category_img","is_active"]
    widgets = {
      'category_name': forms.TextInput(attrs={'class':'form-control'}),
      'slug': forms.TextInput(attrs={'class':'form-control'}),
      'Category_img': forms.ClearableFileInput(attrs={'class':'form-control'}),
      'is_active': forms.CheckboxInput(),
    }

class EditCategoryForm(forms.ModelForm):
      class Meta:
        model = Category
        fields = ["category_name","slug","Category_img"]