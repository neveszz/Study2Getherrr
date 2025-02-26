from django import forms
from .models import Rooms, User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Full Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Email Address'
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Create Password'
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })
    )

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        exclude = ['host', 'participants']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg py-3 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500 transition ease-in-out duration-300',
                'placeholder': 'Enter room name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg py-3 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500 transition ease-in-out duration-300',
                'placeholder': 'Describe your room'
            }),
            'topic': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg py-3 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500 transition ease-in-out duration-300',
            })
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','username', 'email', 'avatar','bio']