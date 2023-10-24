from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateProduct

from .models import Product


def home(request):
    products = Product.objects.all()

    return render(request, "product/home.html", {"products": products})

@login_required
def createproduct(request):
    form = CreateProduct()
    return render(request, 'product/create_product.html', {"form": form})