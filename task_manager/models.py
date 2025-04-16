from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=50)


class TaskType(models.Model):
    name = models.CharField(max_length=50)


class Position(models.Model):
    name = models.CharField(max_length=50)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "Low"
        NORMAL = "Normal"
        HIGH = "High"
        URGENT = "Urgent"

    name = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    task_type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    assignees = models.ManyToManyField(get_user_model(), related_name="assigned_tasks")
    priority = models.CharField(choices=Priority, default=Priority.NORMAL, max_length=10)
    end_date = models.DateTimeField(blank=True, null=True)


    class Meta:
        ordering = ["status", "-date"]# add priority
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
