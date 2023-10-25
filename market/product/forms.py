from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','quantity', 'description','image', 'price', 'location']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','quantity', 'description','image', 'price', 'location']
