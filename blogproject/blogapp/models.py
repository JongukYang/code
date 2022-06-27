from tkinter import CASCADE
from django.db import models

# admin.py 에 작성하면 http 에서 볼 수 있음
# Create your models here.
# 클래스로 정의하고, models안에 Model을 상속받아 사용함
# 이것은 djago에서 제공하는 modelForm
class Blog(models.Model):
    title = models.CharField(max_length=200) # 타이틀의 최대 길이는 200자
    body = models.TextField()
    # 사진을 추가하고싶어
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # upload_to : media/blog_photo 로 저장해줘
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간을 추가하겠다
    # 장고에 primary key 를 설정하지 않았기 때문에 장고가 스스로 기본키를 생성했음 그것이 아마 id 일 것이다

    # 아래 함수를 통해 admin 사이트에서 내가 입력한 title을 보여줌
    def __str__(self):
        return self.title 

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    # 댓을이 어떤 게시물에 달려있는 댓글인지 확인할 수 있는 변수 필요 
    # 따라서 위의 Blog 객체를 참조해야 하는데 이것을 외래키 라고함(foreign key)
    # 코멘트는 블로그의 종속된 것이기 때문에 블로그 포스트가 삭제된다면 같이 삭제한다. 
    # 그것이 on_delete=models.CASCADE
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.comment