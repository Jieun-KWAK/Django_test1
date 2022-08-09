from django.shortcuts import render, redirect
from .models import BLog
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'index.html') 

# 블로그 글 작성 html 보여주는 함수
def new(request):
    return render(request, 'new.html') 

# 블로그 글을 저장해주는 함수로 html render 불필요
def create(request):
    if(request.method == 'POST'):
        post = BLog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now() 
        post.save()
    return redirect('home')