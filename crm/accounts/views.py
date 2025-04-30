from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('product:index')

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('product:index')