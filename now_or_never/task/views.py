import datetime
from django.shortcuts import render

from django.views.generic import ListView, DetailView

from task.models import Task


class TodayTodoView(ListView):
    model = Task
    today = datetime.date.today()
    queryset = Task.objects.filter(completionDate__gt=today)
    template_name = 'task/index.html'


class TodoDetailView(DetailView):
    pass