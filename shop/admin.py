from django.contrib import admin
from .models import Shop, Item
# Register your models here.
@admin.register(Shop)                 # 장식자 (decorate 문법)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_at']
    list_display_links = ['name']
    # list_filter = ['is_publish']
    search_fields = ['name']

    def __str__(self):
        return self.name


    # def short_content(self, shop):
    #     return post.content[:20]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_public', 'created_at', 'shop']
    list_display_links = ['name']
    # list_filter = ['is_publish']
    search_fields = ['name']