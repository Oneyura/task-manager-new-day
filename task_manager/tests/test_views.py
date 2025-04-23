from django.test import TestCase
from django.urls import reverse
from accounts.models import Worker

class TaskListViewTest(TestCase):
    def setUp(self):
        self.user = Worker.objects.create_user(username="admin", password="admin123")
        self.client.login(username="admin", password="admin123")

    def test_task_list_view(self):
        response = self.client.get(reverse("task-manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_list.html")
