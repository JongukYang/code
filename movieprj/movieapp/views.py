from django.shortcuts import render
from .apisecretkey import secret_api_key
import requests, json
from .forms import SearchForm

my_id = secret_api_key

# Create your views here.
def home(request):
    if request.method == 'POST':
        # 입력된 내용을 바탕으로 
        # https://api.themoviedb.org/3/search/movie?api_key=4af39b3a2d55eb242a4ea716a4cc0a1c&page=1&include_adult=false
        # 위 형태의 url로 get 요청 보내기
        form = SearchForm(request.POST)
        searchWord = request.POST.get('search') # search 로서 입력된 값을 가져옴 -> forms.py에 있음
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query=' + searchWord
            response = requests.get(url)
            resdata = response.text
            # 파이썬에서 사용할 수 있는 json 으로 변경
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'resdata':resdata, 'obj':obj})
    else:    
        # 입력 공간 보여주기
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        response = requests.get(url) # <Response [200]> 출력됨
        resdata = response.text # 가공해서 활용하고 싶은 정보, 문자열
        obj = json.loads(resdata) # 파이썬 객체로 사용하기 위해 json으로 변형    
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/'+ movie_id +'?api_key=' + my_id
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {'resdata':resdata})

