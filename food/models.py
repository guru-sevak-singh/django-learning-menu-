from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500,
                             default="https://cdn.shopify.com/s/files/1/0041/3600/9841/files/coming_soon_large.jpg?v=1540936113")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
