from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from task_manager.models import Task, Tag, TaskType, Position


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "assignees",
            "task_type",
            "priority",
            "tags",
        ]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class WorkerForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("position", )


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = (
        ("", "all"),
        ("true", "Completed"),
        ("false", "Not completed")
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
        label="",
        max_length=100,
        required=False,
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label="Tag",
        widget=forms.CheckboxSelectMultiple,
    )
    task_type = forms.ModelMultipleChoiceField(
        queryset=TaskType.objects.all(),
        required=False,
        label="Task Type",
        widget=forms.CheckboxSelectMultiple,
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        label="Status",
    )
    priority = forms.ChoiceField(
        choices=[("", "All priorities")] + list(Task.Priority.choices),
        required=False,
        label = "Priority"
    )
    only_my = forms.BooleanField(
        required=False,
        label="Only my tasks",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )


class WorkerFilterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
        label="",
        max_length=100,
        required=False,
    )
    position = forms.ModelMultipleChoiceField(
        queryset=Position.objects.all(),
        required=False,
        label="Position",
        widget=forms.CheckboxSelectMultiple,
    )
