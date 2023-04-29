from django.urls import path

from users.views import UserLoginView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('logout/', UserLogoutView.as_view(), name='user_logout')
]