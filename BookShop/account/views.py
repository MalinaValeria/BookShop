from django.contrib.auth import views, login
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView

from account.forms import LoginForm, RegisterForm
from account.models import User
from account.tasks import activation_email_task


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

    def form_valid(self, form):
        user = form.save()
        user.save()
        activation_email_task.delay(user.id)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse_lazy('register_done')


class RegisterDoneView(views.TemplateView):
    template_name = 'register_done.html'


class ActivateView(View):
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(self.kwargs['uidb64'])
            user = User.objects.get(pk=uid)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, self.kwargs['token']):
            user.is_active = True
            user.save()
            login(self.request, user)
            return render(self.request, 'activation_done.html')
        else:
            return render(self.request, 'activation_invalid.html')
