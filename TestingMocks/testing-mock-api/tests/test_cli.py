import unittest
from unittest.mock import patch, MagicMock
import json
from app.cli import CLI  


class TestCLI(unittest.TestCase):
    """Тестирование класса CLI."""

    def setUp(self):
        """Настройка окружения для тестов."""
        self.cli = CLI()

    @patch('requests.post')
    def test_registration(self, mock_post):
        """Тестирование метода registration."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "message": "User registered"}
        mock_post.return_value = mock_response

        # Выполнение метода
        self.cli.registration("testuser", "password123")

        # Проверки
        mock_post.assert_called_once_with(
            "http://localhost:8080/registration",
            json={"username": "testuser", "password": "password123"}
        )

    @patch('requests.post')
    def test_registration_error(self, mock_post):
        """Тестирование метода registration с ошибкой."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        # Выполнение метода
        self.cli.registration("testuser", "password123")

        # Проверки
        mock_post.assert_called_once_with(
            "http://localhost:8080/registration",
            json={"username": "testuser", "password": "password123"}
        )

    @patch('requests.post')
    def test_update(self, mock_post):
        """Тестирование метода update."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "message": "User updated"}
        mock_post.return_value = mock_response

        # Выполнение метода
        self.cli.update("testuser", "password123", "Moscow", "25", "reading")

        # Проверки
        mock_post.assert_called_once_with(
            "http://localhost:8080/upload/testuser",
            json={"data": "Password,City,Age,Hobby\npassword123,Moscow,25,reading"}
        )

    @patch('requests.post')
    def test_update_error(self, mock_post):
        """Тестирование метода update с ошибкой."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "User not found"
        mock_post.return_value = mock_response

        # Выполнение метода
        self.cli.update("nonexistent", "password123", "Moscow", "25", "reading")

        # Проверки
        mock_post.assert_called_once_with(
            "http://localhost:8080/upload/nonexistent",
            json={"data": "Password,City,Age,Hobby\npassword123,Moscow,25,reading"}
        )

    @patch('requests.get')
    def test_get_users(self, mock_get):
        """Тестирование метода get_users."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"username": "user1"}, {"username": "user2"}]
        mock_get.return_value = mock_response

        # Выполнение метода
        self.cli.get_users()

        # Проверки
        mock_get.assert_called_once_with("http://localhost:8080/get-users")

    @patch('requests.get')
    def test_get_user(self, mock_get):
        """Тестирование метода get_user."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "username": "testuser",
            "city": "Moscow",
            "age": "25",
            "hobby": "reading"
        }
        mock_get.return_value = mock_response

        # Выполнение метода
        self.cli.get_user("testuser")

        # Проверки
        mock_get.assert_called_once_with("http://localhost:8080/get_information/testuser")

    @patch('requests.get')
    def test_get_user_error(self, mock_get):
        """Тестирование метода get_user с ошибкой."""
        # Настройка мока
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "User not found"
        mock_get.return_value = mock_response

        # Выполнение метода
        self.cli.get_user("nonexistent")

        # Проверки
        mock_get.assert_called_once_with("http://localhost:8080/get_information/nonexistent")

    @patch('questionary.select')
    @patch('questionary.text')
    @patch('questionary.password')
    def test_start_message_registration(self, mock_password, mock_text, mock_select):
        """Тестирование метода start_message для регистрации."""
        # Настройка моков
        mock_select.return_value.ask.side_effect = ["Registration", KeyboardInterrupt]
        mock_text.return_value.ask.side_effect = ["testuser", None]
        mock_password.return_value.ask.return_value = "password123"
        
        # Мокаем метод registration
        self.cli.registration = MagicMock()

        # Вызываем метод с ожиданием прерывания
        try:
            self.cli.start_message()
        except KeyboardInterrupt:
            pass

        # Проверки
        self.cli.registration.assert_called_once_with("testuser", "password123")


if __name__ == '__main__':
    unittest.main()