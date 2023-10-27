from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units =models.IntegerField(default=1)

    def __str__(self):
        return f"{self.units} x {self.product.name}"

    def get_absolute_url(self):
        return reverse('cart:cart_detail')
