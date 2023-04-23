from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView


class UserLoginView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password']
    template_name = 'users/login.html'

