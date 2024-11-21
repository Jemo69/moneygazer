from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def work(request):
    return render(request,'dashboard/home.html',{
        'button_title':'Submit',
        'type':'submit'
    })
def chat(request):
    return render(request,'dashboard/chat.html',{
        'input_buttontext':'Submit',
        'type':"submit",
        'placeholdertext':'ask your question' 
    })