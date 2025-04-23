from django.test import TestCase
from task_manager.models import Task, TaskType
from accounts.models import Worker

class TaskModelTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.user = Worker.objects.create_user(username="john", password="pass1234")
        self.task = Task.objects.create(
            name="Fix login issue",
            task_type=self.task_type,
            status=False,
        )
        self.task.assignees.add(self.user)

    def test_task_creation(self):
        self.assertEqual(self.task.name, "Fix login issue")
        self.assertFalse(self.task.status)
        self.assertIn(self.user, self.task.assignees.all())
