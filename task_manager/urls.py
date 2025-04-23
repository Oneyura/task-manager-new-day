from django.urls import path

from task_manager.views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskAssignView,
    TaskUnassignView,
    TaskCompleteView,
    TaskUndoView,
    SettingsView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/assign/", TaskAssignView.as_view(), name="task-assign"),
    path("tasks/<int:pk>/unassign/", TaskUnassignView.as_view(), name="task-unassign"),
    path("tasks/<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
    path("tasks/<int:pk>/undo/", TaskUndoView.as_view(), name="task-undo"),
    path("settings/", SettingsView, name="settings"),
    path("settings/tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("settings/tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("settings/tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path(
        "settings/task-type/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "settings/task-type/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "settings/task-type/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
]

app_name = "task_manager"
