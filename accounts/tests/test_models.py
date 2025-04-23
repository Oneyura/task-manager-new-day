from django.test import TestCase
from accounts.models import Worker

class WorkerModelTest(TestCase):
    def test_create_worker(self):
        user = Worker.objects.create_user(
            username="jane", password="testpass123", first_name="Jane"
        )
        self.assertEqual(user.username, "jane")
        self.assertTrue(user.check_password("testpass123"))
        self.assertFalse(user.is_staff)
