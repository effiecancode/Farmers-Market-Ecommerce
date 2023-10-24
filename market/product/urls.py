from django.urls import path

from .views import home, create_product


app_name = "product"

urlpatterns = [
    path("", home, name="home"),
    path('create_product/', create_product, name='createproduct')
]