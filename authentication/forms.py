from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="Имя пользователя",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=32, label="Имя",
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    second_name = forms.CharField(max_length=32, label="Фамилия",
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(max_length=32, label="Пароль",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=32, label="Подтвердите пароль",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'password1')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               label="Имя пользователя",
                               widget=forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(max_length=32,
                               label="Пароль",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
