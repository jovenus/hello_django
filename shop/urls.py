from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),              #pk : primary key
    # new shop
    path('new/', views.shop_new, name='shop_new'),
    path('new_cbv/', views.shop_new_cbv, name='shop_new_cbv'),
    # # TODO : edit shop
    path('<int:pk>/edit/', views.shop_edit, name='shop_edit'),
    path('<int:pk>/edit_cbv/', views.shop_edit_cbv, name='shop_edit_cbv'),   
    # # TODO : delete shop
    # path('<int:pk>/del/', views.shop_del),   
]