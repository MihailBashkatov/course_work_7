from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    """ Form for login """
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

class UserRegisterForm(UserCreationForm):
    """ Form for registration """
    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'last_name', 'phone_number', 'password1', 'password2', 'avatar']


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": " Insert email"}
        )

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": " Insert name"}
        )

        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": " Insert last_name"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Insert password"}
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control", "placeholder": "Repeat password"
            }
        )

        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Insert phone number"}
        )

        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Upload avatar"}
        )


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
