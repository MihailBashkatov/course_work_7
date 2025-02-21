from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Login',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input'})
    )
    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input'})
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

