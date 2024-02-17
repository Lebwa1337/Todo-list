from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from todo.forms import TaskForm
from todo.models import Task


def index(request: HttpRequest) -> HttpResponse:

    return render(request, 'todo/index.html')


class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo/task_form.html'
    form_class = TaskForm
