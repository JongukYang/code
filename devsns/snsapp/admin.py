from django.contrib import admin
from .models import Post

# Register your models here.

# 장고에서는 데베 접근을 admin 사이트에서 할 수 있으므로 이렇게 사용
admin.site.register(Post)
