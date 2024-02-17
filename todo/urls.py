from django.urls import path

from todo import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create")
]

app_name = "todo"
