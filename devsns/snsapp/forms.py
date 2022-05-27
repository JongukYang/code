from django import forms
from .models import Post

# 클래스 기반으로 만든다. Models.py 와 같음
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title', 'body']
