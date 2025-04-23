from django import forms

from task_manager.models import Task, Tag, TaskType


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


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = (("", "all"), ("true", "Completed"), ("false", "Not completed"))

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
        # widget=forms.CheckboxSelectMultiple,
    )
    task_type = forms.ModelMultipleChoiceField(
        queryset=TaskType.objects.all(),
        required=False,
        label="Task Type",
        # widget=forms.CheckboxSelectMultiple,
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        label="Status",
    )
    priority = forms.ChoiceField(
        choices=[("", "All priorities")] + list(Task.Priority.choices),
        required=False,
        label="Priority",
    )
    only_my = forms.BooleanField(
        required=False,
        label="Only my tasks",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
