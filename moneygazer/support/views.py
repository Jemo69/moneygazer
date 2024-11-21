from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'support/home.html')
  
def artcile(request):
    pass
def chat(request):
    pass