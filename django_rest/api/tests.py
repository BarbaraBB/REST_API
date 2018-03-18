from django.test import TestCase

import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
# Create your tests here.

class LoginViewTestCase(APITestCase):
    url = reverse("rest_login")

    def setUp(self):
        self.username = "test"
        self.email = "test@test.com"
        self.password = "testtest1"
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_login_without_password(self):
        response = self.client.post(self.url, {"email": self.email})
        self.assertEqual(400, response.status_code)

    def test_login_with_invalid_password(self):
        response = self.client.post(self.url, {"email": self.email, "password": "testtest2"})
        self.assertEqual(400, response.status_code)

    def test_login_with_valid_data(self):
        response = self.client.post(self.url, {"email": self.email, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

class RegisterViewTestCase(APITestCase):
    url = reverse("rest_register")

    def test_register_with_invalid_password_repeat(self):
        user_data = {
            "username": "test",
            "email": "test@test.com",
            "password1": "testtest1",
            "password2": "testtest2"
            }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)
