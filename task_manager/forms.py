from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from task_manager.models import Task


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


# class TaskSearchForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
#         label="",
#         max_length=100,
#         required=False,
#     )
#     tag = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
#         label="",
#         max_length=100,
#         required=False,
#     )