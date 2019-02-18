from django.contrib import admin
from .models import Post, Comment
# from .models import Comment

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content', 'is_publish', 'tags', 'created_at']
    list_display_links = ['title']
    list_filter = ['is_publish']
    search_fields = ['title']


    def short_content(selg, post):
        return post.content[:20]

        



    # pass

# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
