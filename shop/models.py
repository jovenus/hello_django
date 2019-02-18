from django.conf import settings  
from django.db import models

# Create your models here.

class Shop (models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    address = models.CharField(max_length=50)

class Item (models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)