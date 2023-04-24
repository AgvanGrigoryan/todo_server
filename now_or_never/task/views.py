from json import loads

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.views import View

from django.views.generic import ListView, DetailView, UpdateView, CreateView

from task.forms import TaskUpdateForm
from task.models import Task, Folder, Color


class TodayTodoView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/index.html'

    def get_queryset(self):
        curYear = datetime.now(tz=timezone.utc).year
        curMonth = datetime.now(tz=timezone.utc).month
        curDay = datetime.now(tz=timezone.utc).day
        return self.request.user.tasks.filter(completionDate__year=curYear,
                                              completionDate__month=curMonth,
                                              completionDate__day=curDay).order_by('completionDate')


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = self.request.user.folder_set.all()
        context['colors'] = Color.objects.all()
        context['form'] = TaskUpdateForm(instance=context['task'])
        # context['user'] = self.request.user
        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completionDate', 'color', 'folder']
    template_name = 'task/task_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.folder = Folder.objects.get(pk=self.request.POST.get('folder'), user=self.request.user)
        form.instance.color = Color.objects.get(pk=self.request.POST.get('color'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = self.request.user.folder_set.all()
        context['colors'] = Color.objects.all()
        context['user'] = self.request.user
        return context


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task/task_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = self.request.user.folder_set.all()
        context['colors'] = Color.objects.all()
        context['user'] = self.request.user
        return context


class TodoDoneUpdate(LoginRequiredMixin, View):
    def post(self, request, pk=None):
        if pk:
            task = Task.objects.get(pk=pk)
            task.isDone = True if loads(request.body)['is_done'] == 'true' else False
            task.save(update_fields=['isDone'])
            data = {'status': 'success', 'is_done': task.isDone}
            return JsonResponse(data, status=200)
        else:
            return HttpResponse(status=405)
