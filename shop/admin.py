from django.contrib import admin
from .models import Shop, Item
# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    # list_display = ['shop', 'name', 'price']
    # list_display_links = ['name']
    # list_filter = ['is_publish']
    # search_fields = ['name']


    def short_content(self, shop):
        return post.content[:20]