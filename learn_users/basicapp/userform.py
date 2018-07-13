from basicapp.models import Userprofileinfo
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class Userregform(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class Userproinf(ModelForm):
    class Meta():
        model = Userprofileinfo
        fields =('portfolio','picture')
