import datetime
from json import loads

import numpy as numpy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View

from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import DeletionMixin

from task.forms import TaskUpdateForm, FolderCreateForm
from task.models import Task, Folder, Color
from task.permissions import AuthorPermissionMixin


class TodoListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = self.request.user.folder_set.all()
        return context


class TodayTodoView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/index.html'

    def get_queryset(self):
        curYear = timezone.now().year
        curMonth = timezone.now().month
        curDay = timezone.now().day
        return self.request.user.tasks.filter(completionDate__year=curYear,
                                              completionDate__month=curMonth,
                                              completionDate__day=curDay).order_by('completionDate')


class TodoDetailView(AuthorPermissionMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completionDate', 'color', 'folder']
    template_name = 'task/task_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.folder = self.request.user.folder_set.get(pk=self.request.POST.get('folder'))
        form.instance.color = Color.objects.get(pk=self.request.POST.get('color'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = Folder.objects.filter(user=self.request.user)
        context['colors'] = Color.objects.all()
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        if request.user.folder_set.all():
            context = super().get(request, *args, **kwargs)
            return context
        else:
            messages.warning(self.request, "You don't have any folders, create your first folder :)")
            return HttpResponseRedirect(reverse('folder_create'))


class TodoUpdateView(AuthorPermissionMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task/task_update.html'

    def form_valid(self, form):
        form.instance.folder = Folder.objects.get(pk=self.request.POST.get('folder'), user=self.request.user)
        form.instance.color = Color.objects.get(pk=self.request.POST.get('color'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = self.request.user.folder_set.all()
        context['colors'] = Color.objects.all()
        context['user'] = self.request.user
        return context


class TodoDoneUpdate(AuthorPermissionMixin, View):
    def post(self, request, pk=None):
        if pk:
            task = Task.objects.get(pk=pk)
            task.isDone = True if loads(request.body)['is_done'] == 'true' else False
            task.save(update_fields=['isDone'])
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=405)


class TodoDeleteView(AuthorPermissionMixin, DeletionMixin, TemplateView):
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('todo_list')

    def get_object(self):
        self.object = Task.objects.get(pk=self.kwargs.get('pk'))
        return self.object


class FolderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Folder
    form_class = FolderCreateForm
    success_url = reverse_lazy('todo_list')
    template_name = 'task/folder_create.html'
    success_message = "Folder %(name)s was created successfully"

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        sheet = form.save(commit=False)
        sheet.requester = self.request.user
        form.instance.user = self.request.user

        try:
            sheet.save()
        except:
            messages.error(self.request, 'You already have such a folder')
            return super().form_invalid(form)
        return super().form_valid(form)


class TodoFilterView(LoginRequiredMixin, ListView):
    template_name = 'task/task_list.html'

    def get_queryset(self, **kwargs):
        queryset = self.request.user.tasks.all()

        if 'all_folders' not in self.request.GET and 'folder' in self.request.GET:
            queryset = queryset.filter(folder__slug__in=self.request.GET.getlist('folder'))

        if 'date' in self.request.GET:
            start, end = self.request.GET.get('date').split('-')
            start_day,start_month, start_year = numpy.asarray(start.split('/'), dtype='int')
            end_day, end_month, end_year = numpy.asarray(end.split('/'), dtype='int')

            start_date = datetime.datetime(start_year, start_month, start_day)
            end_date = datetime.datetime(end_year, end_month, end_day)
            queryset = queryset.filter(Q(completionDate__gte=start_date) & Q(completionDate__lte=end_date))

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['folders'] = self.request.user.folder_set.all()
        return context
