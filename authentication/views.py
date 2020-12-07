from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms import UserRegistrationForm, UserLoginForm


class Registration(View):
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно")
            return redirect('home')
        print(form.errors)
        messages.error(request, "Ошибка регистрации")
        return render(request, 'authentication/register.html', {'form': form})

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'authentication/register.html', {'form': form})


class UserLogin(View):
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        messages.error(request, "Ошибка входа")
        return render(request, 'authentication/login.html', {'form': form})

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("home")
