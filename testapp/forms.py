from django import forms
from testapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class userform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','password1','password2']
class firform(forms.ModelForm):
    fir = forms.TextInput()
    class Meta:
        model = fir
        fields=['subject','fir']
class prisonerform(forms.ModelForm):
    class Meta:
        model = prisoner
        fields=['name','address','prisoner_aadhar_no','crime','punishment','image']
class visitorform(forms.ModelForm):
    class Meta:
        model = visitor
        fields=['name','visitor_aadhar_no','prisoner_aadhar_no','date_of_visit','image']
class guardform(forms.ModelForm):
    q1=(('DayShift','DayShift'),('NightShift','NightShift'))
    shift=forms.ChoiceField(choices=q1,initial='DayShift')
    class Meta:
        model=guard
        fields='__all__'
class crimeform(forms.Form):
    q1=[]
    temp=prisoner.objects.all().values('crime').distinct()
    for i in temp:
        t=[]
        t.append(i['crime'])
        t.append(i['crime'])
        t=tuple(t)
        q1.append(t)
    q1=tuple(q1)
    Crime=forms.ChoiceField(choices=q1,initial=temp[0]['crime'])
