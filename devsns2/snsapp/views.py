from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def postcreate(request):
    # request 메소드가 Post 일 경우
        # 입력값 저장
    if request.method == 'POST':
        pass
    # request method()가 Get일 경우
        # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_from.html', {'from':form})