from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateProductForm
from .models import Product


def home(request):
    products = Product.objects.all()

    return render(request, "product/home.html", {"products": products})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            print(product)
            product.save()

            messages.success(request, f"{form.cleaned_data['name']} posted!")
            return redirect('product:home')
        else:
            print(form.errors)
            messages.error(request, 'Unsuccessful!')

    form = CreateProductForm()
    
    return render(request, 'product/create_product.html', {"form": form})