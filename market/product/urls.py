from django.urls import path

from .views import home, createproduct


app_name = "product"

urlpatterns = [
    path("", home, name="home"),
    path('createproduct/', createproduct, name='createproduct')
]