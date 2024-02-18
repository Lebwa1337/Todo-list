from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', context={'tasks': tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'todo/task_form.html'
    form_class = TaskForm

    def get_success_url(self) -> str:
        return reverse('todo:index')


class TagListView(generic.ListView):
    model = Tag
    template_name = 'todo/tag_list.html'


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'todo/tag_form.html'
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse('todo:tag-list')
