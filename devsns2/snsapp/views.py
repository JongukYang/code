from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post

# Create your views here.
def home(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # request 메소드가 Post 일 경우
        # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # request method()가 Get일 경우
        # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html' , {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글 저장 기능
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        # filled_form.save() 를 바로 하면 안됌
        # 어떤 게시글에 달려있는 댓글인지 알지 못했기 때문
        finished_form = filled_form.save(commit=False)
        # .post에 어떤 게시글인지 pk 정보를 담아서 save 진행
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id) # 내가 댓글 단 포스트로 redirect 해주기