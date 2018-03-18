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

    def test_register_without_data(self):
        user_data = {
            "username": "",
            "email": "",
            "password1": "",
            "password2": ""
            }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_register_with_invalid_password_repeat(self):
        user_data = {
            "username": "test",
            "email": "test@test.com",
            "password1": "testtest1",
            "password2": "testtest2"
            }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_register_with_valid_data(self):
        user_data = {
            "username": "test",
            "email": "test@test.com",
            "password1": "testtest1",
            "password2": "testtest1"
            }

        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

    def test_register_users_with_unique_data(self):
        user_data1 = {
            "username": "test",
            "email": "test@test.com",
            "password1": "testtest1",
            "password2": "testtest1"
            }

        user_data2 = {
            "username": "test",
            "email": "test@test.com",
            "password1": "testtest1",
            "password2": "testtest1"
            }

        response = self.client.post(self.url, user_data1)
        self.assertEqual(201, response.status_code)

        response = self.client.post(self.url, user_data2)
        self.assertEqual(400, response.status_code)

class UsersViewSetTestCase(APITestCase):
    url = reverse('user-list')

    def setUp(self):
        self.test_user1 = User.objects.create_user(username='test_user1', email='test_user1@test.com',password='test_password1')
        self.test_user2 = User.objects.create_user(username='test_user2', email='test_user2@test.com',password='test_password2')


    def test_users_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)
