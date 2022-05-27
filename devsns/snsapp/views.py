from django.shortcuts import redirect, render
from .forms import PostForm
# 데이터 베이스에서 저장된 포스트를 가져오고 싶어서 쿼리셋 형식으로 가져오기 위해 모델 임포트
from .models import Post

# Create your views here.
def home(request):
    # posts = Post.objects.all() # 그냥 모두 가져오기
    posts = Post.objects.filter().order_by('-date') # 필터를 통한 오름차순
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # 만약 request 메소드가 POST 일 경우 
    if request.method == 'POST' or request.method == 'FILES':
        # 입력값 저장
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    # request 메소드가 GET 일 경우
    else:
        # form 입력 html 띄우기
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})
