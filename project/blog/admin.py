from django.contrib import admin
from .models import BlogPost, Comment, Like

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'pub_date')
    list_display_links = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blogpost', 'author', 'text', 'pub_date')
    list_display_links = ('author',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blogpost', 'author')
    list_display_links = ('blogpost',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)