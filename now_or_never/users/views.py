from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView


class UserLoginView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password']
    template_name = 'users/login.html'


class UserLogoutView(LoginRequiredMixin, View):
    def get(self,request):
        logout(request)
        messages.info(request, 'Logged out successfully!')
        return HttpResponseRedirect(reverse('login_page'))
