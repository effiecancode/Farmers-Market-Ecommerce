from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class Product(models.Model):

    CATEGORIES = (
        ("vegetables", "vegetables"),
        ("fruits", "fruits"),
        ("meat", "meat")
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=25, default="Select a category", choices=CATEGORIES)
    quantity = models.IntegerField(default=5)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products")
    price = models.IntegerField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}-({self.quantity}) by {self.owner}"


