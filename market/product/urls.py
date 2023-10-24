from django.urls import path

from .views import home


app_name = "product"

urlpatterns = [
    path("", home, name="home")
]