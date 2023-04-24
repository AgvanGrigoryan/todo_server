from django.urls import path

from task import views

urlpatterns = [
    path('', views.TodayTodoView.as_view(), name='today'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/detail/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/update/isdone', views.TodoDoneUpdate.as_view(), name='todo_isdone_update'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),

]
