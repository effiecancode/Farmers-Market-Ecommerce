from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.db.models import Q

from django.core.paginator import Paginator

from .forms import CreateProductForm, UpdateProductForm, ProductSearchForm
from .models import Product


def home(request):
    products_list = Product.objects.all().order_by("id")[::-1]
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, "product/home.html", {"products": products})


@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user

            # Check and process the image if it exists
            image = form.cleaned_data.get('image')
            if image:
                img = Image.open(image)
                max_image_size = (500, 500)
                img.thumbnail(max_image_size)
                img_data = BytesIO()
                img.save(img_data, format='JPEG', quality=80)  # You can change format and quality as needed
                img_data.seek(0)

                # Assign the processed image back to the form field
                form.cleaned_data['image'] = InMemoryUploadedFile(
                    img_data,
                    None,
                    image.name,
                    'image/jpeg',
                    img_data.tell(),
                    None
                )

            product.save()
            messages.success(request, f"{form.cleaned_data['name']} posted!", extra_tags="success")
            return redirect('dashboard:index')
        else:
            print(form.errors)
            messages.error(request, 'Unsuccessful!', extra_tags="error")

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

            messages.success(request, "product updated successfully!", extra_tags="success")
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
    messages.warning(request, "product deleted!", extra_tags="warning")

    return redirect('product:home')


def product_search(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        location = form.cleaned_data.get('location')
        category = form.cleaned_data.get('category')

        if name:
            products = products.filter(Q(name__icontains=name))

        if location:
            products = products.filter(Q(location__icontains=location))

        if category and category != 'Select a category':
            products = products.filter(Q(category=category))

    context = {
        'form': form,
        'products': products
    }
    return render(request, 'product/product_search.html', context)

