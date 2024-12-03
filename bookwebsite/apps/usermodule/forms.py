from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password']

    username = forms.CharField(
        #label = 'Username:'
    ) 

    email = forms.EmailField(
        #label = "Email:"
    )
    password = forms.CharField(
        #label = 'Password: '
         widget=forms.PasswordInput
    )

    
class RecoverForm(forms.Form):
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput
    )