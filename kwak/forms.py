from django import forms
# 나중에 나올 부분 일단 지우심 from .models import BLog

class BLogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)