

from dataclasses import fields
from pyexpat import model
from .models import services,Queries,Contact,serviceQuery
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class serviceform(forms.ModelForm):
    class Meta:
        model=services
        fields=('service_name','service_provider','price','contact_number','catogary')

    
class Queryform(forms.ModelForm):
    class Meta:
        model=Queries
        fields=('Query_detail',)




class cntactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('name','email','phone','Desc')

class comform(forms.ModelForm):
    class Meta :
        model=serviceQuery
        fields=('Query_Detail','user','Service')


 
class Userregistrationform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')   