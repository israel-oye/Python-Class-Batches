from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
            'first_name',
            'password',
            'phone_number'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
        self.fields['password'].widget = forms.PasswordInput()

    def save(self, commit = True):
        user: AbstractUser = super().save(commit=False)
        unhashed_pwd = user.password
        user.set_password(unhashed_pwd)
        user.save()
        return user



class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(
        max_length=255, 
        required=True, 
        widget=forms.PasswordInput()
    )

       
        
