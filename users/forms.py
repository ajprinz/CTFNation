from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from dashboard.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Set field attributes
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control form-control-md inverse-mode'})
        self.fields['username'].help_text = '?'
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control form-control-md inverse-mode'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control form-control-md inverse-mode'})
        self.fields['password1'].help_text = '?'
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password Confirmation', 'class': 'form-control form-control-md inverse-mode'})
        self.fields['password2'].help_text = '?'


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control form-control-md inverse-mode'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control form-control-md inverse-mode'})


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']


    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Set field attributes
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
