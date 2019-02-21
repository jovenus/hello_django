from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.shop_detail),              #pk : primary key
    # new shop
    path('new/', views.shop_new),
    # # TODO : edit shop
    # path('<int:pk>/edit', views.shop_edit),   
    # # TODO : delete shop
    # path('<int:pk>/del', views.shop_del),   
]