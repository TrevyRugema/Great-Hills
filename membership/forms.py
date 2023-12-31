from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username=forms.CharField(max_length=50)
    phone_no=forms.IntegerField()
    firs_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)

    class Meta:
        model=Member
        fields=['email','username','mobile_number', 'password','role']
        widget={
            'role':forms.TypedChoiceField(choices=Member.Role)
        }
class LoginForm(UserCreationForm):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)

    class Meta:
        model=Member
        fields=['username','password']
        widget={
            'username':forms.CharField(required=True),
            'password':forms.PasswordInput()
        }
