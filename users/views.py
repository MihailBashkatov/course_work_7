from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
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

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)  # send welcome email
        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = 'Welcome to Mailing App!'
        message = 'Hello  thank you for joining our services!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)