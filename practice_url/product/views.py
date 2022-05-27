from django.shortcuts import render

# Create your views here.
# productlist.html을 띄워주는 함수라고 할 수 있음
def productlist(request):
    return render(request, 'productlist.html')

def productfirst(request):
    return render(request, 'productfirst.html')
