from json import loads

from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth import logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView

from task.models import Folder
from users.forms import UserLoginForm, UserSignupForm, UserUpdateForm
from users.models import User


class UserLoginRegistrationPageView(TemplateView):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.request.user.get_absolute_url())
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = UserLoginForm
        context['reg_form'] = UserSignupForm
        return context


class UserLoginView(View):
    form_class = UserLoginForm

    def post(self, request):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.request.user.get_absolute_url())
        form = self.form_class(data=self.request.POST)
        if form.is_valid():
            username = self.request.POST.get('username', None)
            password = self.request.POST.get('password', None)
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                else:
                    messages.error(self.request, 'Your account is not activated')
            else:
                messages.error(self.request, 'Invalid datas for login')
        else:
            messages.error(self.request, form.errors)
        return HttpResponseRedirect(settings.LOGIN_URL)


class UserCreateView(View):
    form_class = UserSignupForm

    def get(self, request):
        return HttpResponseRedirect(settings.LOGIN_URL)

    def post(self, request):
        user = self.request.user
        if user.is_authenticated:
            return HttpResponseRedirect(self.request.user.get_absolute_url())
        form = self.form_class(data=self.request.POST)
        if form.is_valid():
            created_user = form.save()
            Folder.objects.create(name='All', user=created_user)
            messages.success(request, "You have successfully registered, you can log in")
        else:
            messages.error(self.request, form.errors)
        return HttpResponseRedirect(settings.LOGIN_URL)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/profile.html'
    slug_field = 'username'
    success_url = reverse_lazy('user_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        userform = UserUpdateForm(data=self.request.POST, files=self.request.FILES, instance=self.request.user)
        return super().form_valid(userform)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form_class = self.get_form_class()
    #     context['form'] = form_class(instance=self.request.user)
    #     return context


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Logged out successfully!')
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


class IsUsernameFree(View):
    def post(self, request):
        username = loads(request.body)['username']
        users = User.objects.filter(username=username)
        if users:
            return JsonResponse(data={'status': 'busy'})
        return JsonResponse(data={'status': 'free'})


class IsEmailFree(View):
    def post(self, request):
        email = loads(request.body)['email']
        users = User.objects.filter(email=email)
        if users:
            return JsonResponse(data={'status': 'busy'})
        return JsonResponse(data={'status': 'free'})
