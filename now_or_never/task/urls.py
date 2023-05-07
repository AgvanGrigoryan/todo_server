from django.urls import path

from task import views

urlpatterns = [
    path('', views.TodayTodoView.as_view(), name='today'),
    path('list/', views.TodoListView.as_view(), name='todo_list'),
    path('filter/', views.TodoFilterView.as_view(), name='todo_filter'),
    path('search/', views.TodoSearchView.as_view(), name='todo_search'),
    path('create/folder', views.FolderCreateView.as_view(), name='folder_create'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/detail/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/update/isdone', views.TodoDoneUpdate.as_view(), name='todo_isdone_update'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),


]
