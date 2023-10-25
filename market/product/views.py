from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateProductForm, UpdateProductForm
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
            # print(product)
            product.save()

            messages.success(request, f"{form.cleaned_data['name']} posted!")
            return redirect('product:home')
        else:
            print(form.errors)
            messages.error(request, 'Unsuccessful!')

    form = CreateProductForm()

    return render(request, 'product/create_product.html', {"form": form})


def product_details(request, id):
    product = Product.objects.get(id=id)
    # print(product)
    items = Product.objects.filter(category=product.category)
    return render(request, "product/product_details.html", {'product': product, 'items': items,})


@login_required
def update_product(request, id):

    product = get_object_or_404(Product, id=id, owner=request.user)

    if request.method == "POST":
        form = UpdateProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect("product:product_details", id=product.id)
    else:
        form = UpdateProductForm(instance=product)

    context = {
        "form": form
    }

    return render(request, "product/update_product.html", context)

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id, owner=request.user)
    product.delete()

    return redirect('product:home')