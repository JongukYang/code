from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def showme(request):
    return render(request, 'showme.html')    