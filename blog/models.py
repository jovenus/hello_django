from django.db import models

# Create your models here.
class Post(models.Model):
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