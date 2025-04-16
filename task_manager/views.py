from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic, View

from task_manager.forms import TaskForm, WorkerForm, TaskSearchForm
from task_manager.models import Task, Worker, Tag, TaskType, Position


def index(request):
    now = timezone.now()
    tasks = Task.objects.all()
    count_tasks = tasks.count()
    count_workers = Worker.objects.all().count()
    count_completed_tasks = tasks.filter(status=True).count()
    count_terminated_tasks = tasks.filter(
        deadline__lt=now
    ).count()
    count_active_tasks = tasks.filter(
        deadline__gt=now, status=False
    ).count()
    count_completed_tasks_by_7days = {
        (now - timedelta(days=day)).date(): tasks.filter(
            end_date__date=(now - timedelta(days=day)).date(),
            status=True
        ).count()
        for day in range(7)
    }
    count_terminated_tasks_by_7days = {
        (now - timedelta(days=day)).date(): tasks.filter(
            deadline__date=(now - timedelta(days=day)).date(),
            status=False
        ).count()
        for day in range(7)
    }
    context = {
        "count_tasks": count_tasks,
        "count_workers": count_workers,
        "count_completed_tasks": count_completed_tasks,
        "count_terminated_tasks": count_terminated_tasks,
        "count_active_tasks": count_active_tasks,
        "count_completed_tasks_by_7days": count_completed_tasks_by_7days,
        "count_terminated_tasks_by_7days": count_terminated_tasks_by_7days,
    }
    return render(
        request,
        "task_manager/index.html",
        context=context
    )


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    paginate_by = 10
    template_name = "task_manager/task_list.html"

    # search implement and fiter
    # def get_context_data(self, **kwargs):
    #     context = super(TaskListView, self).get_context_data(**kwargs)
    #     name = self.request.GET.get("name", "")
    #     context["search_form"] = TaskSearchForm(initial={"name": name})
    #     return context
    #
    # def get_queryset(self, **kwargs):
    #     form = TaskSearchForm(self.request.GET)
    #     self.queryset = Task.objects.all()
    #     if form.is_valid():
    #         return self.queryset.filter(
    #             name__icontains=form.cleaned_data["name"]
    #         )
    #     return self.queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    from_class = TaskForm
    success_url = reverse_lazy("task-manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-manager:task-list") # add back to last page


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task-manager:task-list")


class TaskAssignView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.assignees = task.assignees.all() + request.user
        task.save()
        return redirect("task-manager:task-list") # add back to last page

class TaskUnassignView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.assignees.remove(request.user)
        task.save()
        return redirect("task-manager:task-list") # add back to last page


class TaskCompleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.status = True
        task.end_date = timezone.now()
        task.save()
        return redirect("task-manager:task-list") # add back to last page

class TaskUndoView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.status = False
        task.save()
        return redirect("task-manager:task-list") # add back to last page


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    paginate_by = 10
    template_name = "task_manager/worker_list.html"
    # search implement and fiter


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("task-manager:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    success_url = reverse_lazy("task-manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task-manager:worker-list")


@login_required
def settings(request):
    context = {
        "tag_list": Tag.objects.all(),
        "task_type_list": TaskType.objects.all(),
        "position_list": Position.objects.all(),
    }
    return render(
        request,
        "task_manager/settings.html",
        context=context
    )


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    success_url = reverse_lazy("task-manager:settings")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("task-manager:settings")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task-manager:settings")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    success_url = reverse_lazy("task-manager:settings")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    success_url = reverse_lazy("task-manager:settings")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task-manager:settings")


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    success_url = reverse_lazy("task-manager:settings")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    success_url = reverse_lazy("task-manager:settings")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task-manager:settings")









