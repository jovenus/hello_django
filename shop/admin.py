from django.contrib import admin
from .models import Shop, Item
# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_display_links = ['name']
    # list_filter = ['is_publish']
    search_fields = ['name']


    # def short_content(self, shop):
    #     return post.content[:20]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'shop']
    list_display_links = ['name']
    # list_filter = ['is_publish']
    search_fields = ['name']