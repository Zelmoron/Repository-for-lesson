import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'testing-mock-api')))

import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.routers import router, users

client = TestClient(router)

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        global users
        users.clear()

    def test_registration_success(self):
        response = client.post("/registration", json={"username": "testuser", "password": "password"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["Username"], "testuser")
        self.assertEqual(data["message"], "registration successful")
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]["Username"], "testuser")
        self.assertEqual(users[0]["Password"], "password")
        self.assertEqual(users[0]["City"], "")
        self.assertEqual(users[0]["Age"], 0)
        self.assertEqual(users[0]["Hobby"], "")

    def test_registration_user_exists(self):
        client.post("/registration", json={"username": "testuser", "password": "password"})
        response = client.post("/registration", json={"username": "testuser", "password": "anotherpassword"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "this user already exists")
        self.assertEqual(len(users), 1)

    def test_get_users(self):
        client.post("/registration", json={"username": "testuser", "password": "password"})
        response = client.get("/get-users")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Username"], "testuser")
        self.assertEqual(data[0]["Password"], "password")
        self.assertEqual(data[0]["City"], "")
        self.assertEqual(data[0]["Age"], 0)
        self.assertEqual(data[0]["Hobby"], "")