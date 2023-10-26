from django.shortcuts import render

from product.models import Product

def index(request):
    products = Product.objects.filter(owner=request.user)

    return render(request, 'dashboard/index.html', {'products': products})
