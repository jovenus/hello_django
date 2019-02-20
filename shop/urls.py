from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.shop_detail),              #pk : primary key
]