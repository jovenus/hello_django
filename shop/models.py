from django.conf import settings  
from django.db import models
from django.urls import reverse

# Create your models here.

class Shop (models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    desc = models.TextField(blank=True)
    address = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        # return "/shop/{}/".format(self.id)
        return reverse("shop:shop_detail", args=[self.id])
        # return reverse("shop:shop_detail", kwargs={'pk': self.id})



class Item (models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name