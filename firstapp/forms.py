from django import forms
from django.contrib.auth.models import User
from .models import Post, Client, History


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'text')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'login', 'password', 'pol', 'age', 'mail')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('author', 'result')
