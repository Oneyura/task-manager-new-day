import random
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.models import Position
from task_manager.models import Task, Tag, TaskType

# Create Tags
for i in range(10):
    Tag.objects.get_or_create(name=f"Tag {i+1}")

# Create Task Types
for i in range(5):
    TaskType.objects.get_or_create(name=f"Type {i+1}")

# Create Positions
for i in range(5):
    Position.objects.get_or_create(name=f"Position {i+1}")

# Create Workers
for i in range(10):
    get_user_model().objects.get_or_create(
        username=f"user{i+1}",
        defaults={
            "first_name": f"First{i+1}",
            "last_name": f"Last{i+1}",
            "email": f"user{i+1}@example.com",
            "position": random.choice(Position.objects.all()),
        }
    )

# Create Tasks
now = timezone.now()
tags = list(Tag.objects.all())
task_types = list(TaskType.objects.all())
workers = list(get_user_model().objects.all())

for i in range(30):
    deadline = now - timedelta(days=random.randint(0, 7))
    task = Task.objects.create(
        name=f"Generated Task {i + 1}",
        description=f"Auto-generated task number {i + 1}",
        deadline=deadline,
        task_type=random.choice(task_types),
        priority=random.choice([choice[0] for choice in Task.Priority.choices]),
        status=random.choice([True, False]),
        end_date=deadline if random.choice([True, False]) else None
    )
    task.tags.set(random.sample(tags, k=random.randint(1, min(3, len(tags)))))
    task.assignees.set(random.sample(workers, k=random.randint(1, min(2, len(workers)))))
    task.save()

print("✅ Dummy data successfully populated.")
