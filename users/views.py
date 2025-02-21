from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, UserRegisterForm
from users.models import User


class LoginUser(LoginView):
    """ Class for login users """
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}


class RegisterUser(CreateView):
    """ Class for registering users"""
    model = User
    extra_context = {'title': 'Register'}
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')