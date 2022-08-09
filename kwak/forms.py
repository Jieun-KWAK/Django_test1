from django import forms
from .models import BLog

class BLogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BLogModelForm(forms.ModelForm):
    class Meta:
        model = BLog
        fields = '__all__'
        #fields = ['title', 'body']