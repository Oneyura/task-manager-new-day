from django.urls import path

from accounts.views import (
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
)

app_name = "accounts"

urlpatterns = [
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path(
        "settings/position/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "settings/position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "settings/position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
]
