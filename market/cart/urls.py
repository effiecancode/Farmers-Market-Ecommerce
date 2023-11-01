from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path("addtocart/<int:product_id>/", views.add_to_cart, name='addtocart'),
    path("removefromcart/<int:cart_item_id>/", views.remove_from_cart, name='removefromcart'),
    path("cart_detail", views.cart_detail, name='cart_detail'),

    path('increment_units/<int:cart_item_id>/', views.increment_units, name='increment_units'),
    path('decrement_units/<int:cart_item_id>/', views.decrement_units, name='decrement_units'),

    path("mpesa_pay/<int:id>/", views.mpesa_pay, name='mpesa_pay'),
]
