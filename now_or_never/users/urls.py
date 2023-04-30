from django.conf import settings
from django.urls import path

from users.views import UserLoginRegistrationPageView, UserLogoutView, UserLoginView, UserCreateView

urlpatterns = [
    path('login_page/', UserLoginRegistrationPageView.as_view(), name='login_page'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('signup/', UserCreateView.as_view(), name='user_signup'),
    path('logout/', UserLogoutView.as_view(), name='user_logout')
]