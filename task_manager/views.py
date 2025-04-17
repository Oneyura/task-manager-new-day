from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic, View

from task_manager.forms import TaskForm, WorkerForm, WorkerFilterForm, TaskFilterForm
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
    count_completed_tasks_for_7days = {
        (now - timedelta(days=day)).date(): tasks.filter(
            end_date__date=(now - timedelta(days=day)).date(),
            status=True
        ).count()
        for day in range(7)
    }
    count_terminated_tasks_for_7days = {
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
        "count_completed_tasks_for_7days": count_completed_tasks_for_7days,
        "count_terminated_tasks_for_7days": count_terminated_tasks_for_7days,
        "labels_7days": list(reversed([date.strftime("%Y-%m-%d") for date in count_completed_tasks_for_7days.keys()])),
        "completed_data": list(reversed(list(count_completed_tasks_for_7days.values()))),
        "terminated_data": list(reversed(list(count_terminated_tasks_for_7days.values()))),
    }
    return render(
        request,
        "task_manager/index.html",
        context=context
    )


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_manager/task_list.html"

    # search implement and fiter
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        tag = self.request.GET.get("tag", "")
        task_type = self.request.GET.get("task_type", "")
        status = self.request.GET.get("status", "")
        priority = self.request.GET.get("priority", "")
        only_my = self.request.GET.get("only_my", "")
        context["filter_form"] = TaskFilterForm(
            initial={
                "name": name,
                "tag": tag,
                "task_type": task_type,
                "status": status,
                "priority": priority,
                "only_my": only_my,
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TaskFilterForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data["name"]
            tag = form.cleaned_data["tag"]
            task_type = form.cleaned_data["task_type"]
            status = form.cleaned_data["status"]
            priority = form.cleaned_data["priority"]
            only_my = form.cleaned_data["only_my"]

            if name:
                queryset = queryset.filter(name__icontains=name)

            if tag:
                queryset = queryset.filter(tags__in=tag).distinct()

            if task_type:
                queryset = queryset.filter(task_type__in=task_type).distinct()

            if status == "true":
                queryset = queryset.filter(status=True)
            elif status == "false":
                queryset = queryset.filter(status=False)

            if priority:
                queryset = queryset.filter(priority=priority)

            if only_my:
                queryset = queryset.filter(
                    assignees=self.request.user
                ).distinct()

        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
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
        task.assignees.add(request.user)
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
    success_url = reverse_lazy("task-manager:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm
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
    fields = "__all__"
    success_url = reverse_lazy("task-manager:settings")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task-manager:settings")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task-manager:settings")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task-manager:settings")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task-manager:settings")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task-manager:settings")


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









