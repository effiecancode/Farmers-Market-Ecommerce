from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics")
    bio = models.TextField()

    def __str__(self):
        return self.user.username


