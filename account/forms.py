from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = USER_MODEL
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
