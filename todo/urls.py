from django.urls import path

from todo import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "todo"
