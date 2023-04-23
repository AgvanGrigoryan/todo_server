from django.urls import path

from task import views

urlpatterns = [
    path('', views.TodayTodoView.as_view(), name='today'),
    path('todo/create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/detail/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),

]
