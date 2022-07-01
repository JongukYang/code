from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # upload = 

    def __str__(self):
        return self.title

# 클래스를 이용해 데이터베이스에 Mapping 하는 것을 ORM(Object Oriented Mapping)
class Comment(models.Model):
    comment = models.TextField(200)
    date = models.DateTimeField(auto_now_add=True)
    # 포스트에 종속적인게 댓글이기 때문에 Foreign키로 작성해주는게 중요
    # 먼저 어떤 포스트인지 찾고
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

# 자유게시판
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField(200)
    date = models.DateTimeField(auto_now_add=True)
    # 포스트에 종속적인게 댓글이기 때문에 Foreign키로 작성해주는게 중요
    # 먼저 어떤 포스트인지 찾고
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment