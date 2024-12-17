# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    account_no = forms.CharField(max_length=20, required=True, help_text='Enter a unique account number.')

    class Meta:
        model = CustomUser
        fields = ('username', 'account_no', 'password1', 'password2')
