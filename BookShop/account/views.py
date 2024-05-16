from django.contrib.auth import views
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from account.forms import LoginForm, RegisterForm


class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('main')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class LogoutView(views.LogoutView):
    def get_next_page(self):
        return self.request.META.get('HTTP_REFERER')


class RegisterView(CreateView):
    template_name = 'register.html'
    model = 'account.User'
    form_class = RegisterForm

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        return redirect('main')
