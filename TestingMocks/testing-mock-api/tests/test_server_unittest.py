import sys
import os
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.routers import router, users

# Добавляем путь к модулю
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'testing-mock-api'))
)

# Создаем клиент для тестирования
client = TestClient(router)


class TestUserEndpoints(unittest.TestCase):
    """
    Тесты для пользовательских эндпоинтов.
    """

    def setUp(self) -> None:
        """
        Очистка списка пользователей перед каждым тестом.
        """
        global users
        users.clear()

    def test_registration_success(self) -> None:
        """
        Тест успешной регистрации пользователя.
        """
        # Данные для регистрации
        registration_data = {"username": "testuser", "password": "password"}

        # Отправляем POST-запрос на регистрацию
        response = client.post("/registration", json=registration_data)

        # Проверяем статус ответа
        self.assertEqual(response.status_code, 200)

        # Извлекаем данные из ответа
        data = response.json()

        # Проверяем содержимое ответа
        self.assertEqual(data["Username"], "testuser")
        self.assertEqual(data["message"], "registration successful")

        # Проверяем, что пользователь добавлен в список
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]["Username"], "testuser")
        self.assertEqual(users[0]["Password"], "password")
        self.assertEqual(users[0]["City"], "")
        self.assertEqual(users[0]["Age"], 0)
        self.assertEqual(users[0]["Hobby"], "")

    def test_registration_user_exists(self) -> None:
        """
        Тест попытки зарегистрировать существующего пользователя.
        """
        # Регистрируем пользователя
        client.post("/registration", json={"username": "testuser", "password": "password"})

        # Данные для повторной регистрации
        registration_data = {"username": "testuser", "password": "anotherpassword"}

        # Отправляем POST-запрос на регистрацию
        response = client.post("/registration", json=registration_data)

        # Проверяем статус ответа
        self.assertEqual(response.status_code, 200)

        # Извлекаем данные из ответа
        data = response.json()

        # Проверяем содержимое ответа
        self.assertEqual(data["message"], "this user already exists")

        # Проверяем, что пользователей осталось один
        self.assertEqual(len(users), 1)

    def test_get_users(self) -> None:
        """
        Тест получения списка пользователей.
        """
        # Регистрируем пользователя
        client.post("/registration", json={"username": "testuser", "password": "password"})

        # Отправляем GET-запрос на получение пользователей
        response = client.get("/get-users")

        # Проверяем статус ответа
        self.assertEqual(response.status_code, 200)

        # Извлекаем данные из ответа
        data = response.json()

        # Проверяем содержимое ответа
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Username"], "testuser")
        self.assertEqual(data[0]["Password"], "password")
        self.assertEqual(data[0]["City"], "")
        self.assertEqual(data[0]["Age"], 0)
        self.assertEqual(data[0]["Hobby"], "")


if __name__ == "__main__":
    unittest.main()