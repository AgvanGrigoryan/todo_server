
from django.shortcuts import render
from django.utils import timezone
from django.utils.datetime_safe import datetime

from django.views.generic import ListView, DetailView

from task.models import Task


class TodayTodoView(ListView):
    model = Task
    today = datetime.now(tz=timezone.utc).day
    queryset = Task.objects.filter(completionDate__day=today)
    template_name = 'task/index.html'


class TodoDetailView(DetailView):
    model = Task
    # def get(self, request, *args, **kwargs):
    #     model = Task
    #     getqueryset = Task.objects.get(pk=request.GET.get('pk'))