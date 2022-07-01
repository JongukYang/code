from django.contrib import admin
from .models import Post, Comment, FreePost, FreeComment
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)