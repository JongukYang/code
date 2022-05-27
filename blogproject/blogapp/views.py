from turtle import title
# pk 값을 이용해 특정 모델 객체 하나만 가져오는 클래스 : get_boject_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
# .foms 의 . 은 같은 폴더라는 뜻
from .forms import BlogFrom, BlogModelForm, CommentForm


# Create your views here.
def home(request):
    # 블로그 글들을 모두 index.html 에 띄우는 방법
    # posts 변수에 Blog객체 모두 저장
    posts = Blog.objects.all()
    # 날짜를 통해 정렬된 형태 '-'를 붙이면 순서가 반대로 (내림차순)
    Blog.objects.filter().order_by('date')
    # 딕셔너리 형태로 추가
    return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save() # 저장
    return redirect('home') # 위의 내용이 진행이 끝나면 다시 home으로 가라~
   

# 장고 폼을 이용하여 입력값을 받는 함수
# Get 요청과 ( = 입력값을 받을 수 있는 html을 가져다 줘야함 )
# Post 요청 ( = 입력한 내용을 데이터베이스에 저장하는 기능을 수행해야함. form에서 입력한 내용을 처리 )
# 둘 다 처리가 가능한 함수
# 장고는 하나의 url에서 GET 요청과 POST 요청을 모두 처리할 수 있음
def formcreate(request):
    if (request.method == 'POST'):
        # 입력 내용을 DB에 저장
        form = BlogFrom(request.POST)
        # 데이터 형식 검사, 입력값의 유효성 검사 
        if form.is_valid():
            # 저장
            post = Blog()
            post.title = form.cleaned_data['title'] # cleaned_data = 검증되었다는 뜻 그냥 선언한거임
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 가져다 주기
        form = BlogFrom()
    # render()의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있습니다.
    # 단, 딕셔너리 자료형으로 넘겨줘야함
    return render(request, 'form_create.html', { 'htmlform':form } )

# 폼조차 자동으로 만들어주는 modelForm
def modelformcreate(request):
    if (request.method == 'POST') or (request.method =='FILES'):
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        # 데이터 형식 검사, 입력값의 유효성 검사 
        if form.is_valid():
            # 저장
            # model Form 으로 만든 것들은 form 자체적으로 save() 메소드가 있음
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 가져다 주기
        form = BlogModelForm()
    # render()의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있습니다.
    # 단, 딕셔너리 자료형으로 넘겨줘야함
    return render(request, 'form_create.html', {'form':form})

# 결국 create 함수는 모델을 기반으로 만든 post 객체를 save 한 것
# 하지만 modelForm은 폼 자체가 save 메소드를 가지고 있어 쉽게 처리 가능

# detail 함수는 인자 값을 request 와 blog_id  두 가지를 가짐
# blog_id 는 post.id 값(즉 기본키 값) 을 받아서 detail 함수를 실행하게 됨
def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 가져와서 
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    # 아래 코드 : 볼로그 객체를 가져올건데 어떤 객체냐? pk=blog_id 인 객체만 가져오겠다 라는 뜻
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        # 우리는 어떤 게시글의 댓글인지를 명시해줘야하기 때문에 아직 저장하지 말라는 아래 코드 작성
        finished_form = filled_form.save(commit=False) 
        # Blog라는 객체의 특정 게시글(blog_id)을 가져와서 finished_form의 post에 넣어준다. 
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        # 어떤 게시글인지 표시했으니 저장해줌
        finished_form.save()

    return redirect('detail', blog_id)
