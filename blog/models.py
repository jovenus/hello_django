from django.conf import settings    # 설정값을 가져오는 올바른 방법
from django.db import models
# from django.comtrib.auth.models import User   #별로 추천하지 않음


settings.AUTH_USER_MODEL
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    tags = models.CharField(max_length=20)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    # pass

    # class Meta:                  #migration 대상에서 빼고 싶을 때 지정
    #     manaaged = False 

class Comment (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""
class Zipcode(models,Model):
    # code = models.CharField(max_length=6, primary_key=True) # Primary 키로 지정
    code = models.CharField(max_length=6, unique=True)
    desc = models.TextField()
"""

# class Shop (models.Model):
#     name = CharField(max_length=100)
#     desc = TextField(blank=True)
#     address = CharField(max_length=50)

# class Item (models.Model):
#     shop = ForeignKey(Shop, on_delete=models.CASCADE)
#     name = CharField(max_length=100)
#     desc = TextField(blank=True)
#     price = PositiveIntegerField()
#     is_public = BooleanField(default=False)