from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'id': 'login_username', "autofocus": True, "placeholder": "Username", "class": "forms_field-input", "required": True}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(
        attrs={"autocomplete": "current-password", "placeholder": "Password", "class": "forms_field-input",
               "required": True}))


class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    username = UsernameField(widget=forms.TextInput(attrs={'id': 'reg_username', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('first_name', 'username','email','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'forms_field-input'
