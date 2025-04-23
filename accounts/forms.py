from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Position


class WorkerForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("position",)


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
