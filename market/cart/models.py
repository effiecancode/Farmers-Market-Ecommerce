from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units =models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.units} x {self.product.name}"
    
    def save(self, *args, **kwargs):
        if self.product.unit_price is not None:
            self.total_price = self.product.unit_price * self.units
        super(Cart, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('cart:cart_detail')




