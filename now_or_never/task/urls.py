from django.urls import path

from task import views

urlpatterns = [
    path('today/', views.TodayTodoView.as_view(), name='today'),
    path('todo/<int:pk>/detail/', views.TodoDetailView.as_view(), name='todo_detail')
]
