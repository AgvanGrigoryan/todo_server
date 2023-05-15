from django.conf import settings
from django.urls import path

from users.views import UserLoginRegistrationPageView, UserLogoutView, UserLoginView, UserCreateView, IsUsernameFree, \
    IsEmailFree, UserUpdateView, UserDetailView

urlpatterns = [
    path('login_page/', UserLoginRegistrationPageView.as_view(), name='login_page'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('signup/isUsernameFree/', IsUsernameFree.as_view(), name='user_signup'),
    path('signup/isEmailFree/', IsEmailFree.as_view(), name='user_signup'),
    path('signup/', UserCreateView.as_view(), name='user_signup'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('profile/', UserDetailView.as_view(), name='user_profile'),
    # path('<slug:slug>/profile/', UserDetailView.as_view(), name='user_profile'),
    path('profile/edit/', UserUpdateView.as_view(), name='user_profile_edit'),
]