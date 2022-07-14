from django.shortcuts import render
from .apisecretkey import secret_api_key

my_id = secret_api_key

# Create your views here.
def home(request):
    return render(request, 'index.html')