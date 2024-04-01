from django.test import TestCase
from django.contrib.auth.models import User
from task_board.models import Task
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
import json


class TaskAPITest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="lauren", email="test@example.com", password="password123"
        )

        # Ensure a token is generated for the user
        Token.objects.create(user=self.user)

        # Authenticate the client with the test user's token
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        # Create some tasks for testing
        self.task1 = Task.objects.create(
            title="Task 1", description="Description for Task 1"
        )
        self.task2 = Task.objects.create(
            title="Task 2", description="Description for Task 2"
        )

    def test_get_all_tasks(self):
        # Send GET request to the tasks endpoint
        response = self.client.get("/tasks/")

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the correct number of tasks
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        # Data to create a new task
        data = {"title": "New Task", "description": "Description for New Task"}

        # Send POST request to create a new task
        response = self.client.post(
            "/tasks/", data=json.dumps(data), content_type="application/json"
        )

        # Check that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the new task is created with the correct data
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().title, "New Task")

    def test_update_task(self):
        # Data to update an existing task
        data = {"title": "Updated Task", "description": "Updated Description"}

        # Send PUT request to update an existing task
        response = self.client.put(
            f"/tasks/{self.task1.pk}/",
            data=json.dumps(data),
            content_type="application/json",
        )

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the task is updated with the correct data
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Updated Task")

    def test_delete_task(self):
        # Send DELETE request to delete an existing task
        response = self.client.delete(f"/tasks/{self.task1.pk}/")

        # Check that the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that the task is deleted
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())

    def test_logout(self):
        # Now, log out
        response = self.client.post("http://127.0.0.1:8000/logout/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # After logout, attempt to access a protected resource
        response = self.client.get("http://127.0.0.1:8000/tasks/")
        # Assert that accessing protected resource after logout is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
