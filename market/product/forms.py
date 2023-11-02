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


class ProductSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Search by name')
    location = forms.CharField(required=False, label='Search by location')
    category_choices = list(Product.CATEGORIES)  # Convert to a list
    category = forms.ChoiceField(
        required=False,
        label='Category',
        choices=[('', 'Select a category')] + category_choices
    )

