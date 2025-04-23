from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import WorkerFilterForm, WorkerForm
from accounts.models import Worker, Position


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task_manager/worker_list.html"

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        position = self.request.GET.get("position", "")
        context["filter_form"] = WorkerFilterForm(
            initial={"username": username, "position": position}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = WorkerFilterForm(self.request.GET)

        if form.is_valid():
            username = form.cleaned_data["username"]
            position = form.cleaned_data["position"]

            if username:
                queryset = queryset.filter(username__icontains=username)

            if position:
                queryset = queryset.filter(position__in=position).distinct()

        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("accounts:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("accounts:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("accounts:worker-list")


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task-manager:settings")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task-manager:settings")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task-manager:settings")
