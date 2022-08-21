from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from virtual_library.models import User, Book

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['owner']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
