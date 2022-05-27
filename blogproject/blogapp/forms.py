from dataclasses import field
from django import forms
from .models import Blog, Comment

class BlogFrom(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

# 폼 조차 자동으로 생성해주는 ModelForm 
# 모델은 models.py/Blog() 폼을 가져옴
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' # 모든 것들을 필드 모델로서 사용
        # fields = ['title', 'body'] # 특정 필드만을 사용하려면 리스트형으로
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__' # 모든 것들을 필드 모델로서 사용
        fields = ['comment']