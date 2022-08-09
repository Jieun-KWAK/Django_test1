from django.shortcuts import render, redirect
from .models import BLog
from django.utils import timezone
from .forms import BLogForm, BLogModelForm

# Create your views here.
def home(request):
    return render(request, 'index.html') 

# html form 이용 
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

# Django form 이용
# GET요청 (= 입력값을 받을 수 있는 html을 갖다 줘야함)
# POST요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리 가능한 함수
def formcreate(request):
    if request.method == 'POST':
        form = BLogForm(request.POST)
        if form.is_valid():
            post = BLog()
            post.title = form.cleaned_data['title']
            post.title = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:  
        form = BLogForm
    return render(request, 'form_create.html', {'form': form})

# modelformcreate
def modelformcreate(request):
    #입력을 받을 수 있는 html을 갖다주기
    if request.method == 'POST':
        form = BLogModelForm(request.POST)
        if form.is_valid():  #유효성 판단 _vaild()
            form.save()
            return redirect('home')
    else:
        form = BLogModelForm()
    return render(request, 'form_create.html', {'form':form})