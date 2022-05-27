from django.db import models

# Create your models here.
# 글들의 목록 출력
# 게시물 모델

class Post(models.Model):
    title = models.CharField(max_length=200) # 게시물의 제목
    body = models.TextField() # 게시물의 본문
    date = models.DateTimeField(auto_now_add=True) # 날짜 시간

    def __str__(self):
        return self.title