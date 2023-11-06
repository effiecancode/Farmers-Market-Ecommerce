from django.urls import path

from . import views


app_name = "product"

urlpatterns = [
    path("", views.home, name="home"),
    path('create_product/', views.create_product, name='create_product'),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),

    path("product_search/", views.product_search, name="product_search"),
]