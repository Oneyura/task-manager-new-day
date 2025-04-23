from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import (
    Task,
    Worker,
    Tag,
    Position,
    TaskType
)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Worker, UserAdmin)
admin.site.register(Tag)
admin.site.register(Position)
admin.site.register(TaskType)

