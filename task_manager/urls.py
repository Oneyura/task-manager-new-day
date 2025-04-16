from django.urls import path, include

from task_manager.models import TaskType

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(), name="task-detail"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/assign/",
        TaskAssignView.as_view(),
        name="task-assign"
    ),
    path(
        "tasks/<int:pk>/unassign/",
        TaskUnassignView.as_view(),
        name="task-unassign"
    ),
    path(
        "tasks/<int:pk>/complete/",
        TaskCompleteView.as_view(),
        name="task-complete"
    ),
    path(
        "tasks/<int:pk>/undo/",
        TaskUndoView.as_view(),
        name="task-undo"
    ),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),

    path(
        "settings/",
        settings,
        name="settings"
    ),
    path(
        "settings/tag/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "settings/tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "settings/tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "settings/task-type/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "settings/task-type/<int:pk>/update/",
        TaskTypeCreateView.as_view(),
        name="task-type-update"
    ),
    path(
        "settings/task-type/<int:pk>/delete/",
        TaskTypeCreateView.as_view(),
        name="task-type-delete"
    )
    path(
        "settings/position/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "settings/position/<int:pk>/update/",
        PsitionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "settings/position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete"
    )
]

app_name = "task_manager"
