from django.urls import path

from .views import home, create_product, product_details


app_name = "product"

urlpatterns = [
    path("", home, name="home"),
    path('create_product/', create_product, name='create_product'),
    path('product_details/<int:id>/', product_details, name='product_details')
]