from django.urls import path

from todo import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
]

app_name = "todo"
