import questionary
import requests

class CLI:
    """
    Command Line Interface (CLI) class for user interaction.

    This class provides methods for user registration, updating user data with CSV,
    retrieving all users, and getting specific user information.
    """

    def __init__(self):
        """
        Initializes the CLI object.

        Currently, this method does not perform any actions.
        """
        pass

    def start_message(self):
        """
        Starts the CLI interaction loop.

        Presents the user with a menu to choose from:
        - Registration
        - Update with CSV
        - Get all users
        - Get specific user

        Based on the user's choice, it calls the corresponding method.
        """
        while True:
            command = questionary.select(
                "What do you want to do?",
                choices=["Registration", "Update with csv", "Get all users", "Get specific user"],
            ).ask()
            
            if command == "Registration":
                name = questionary.text("What's your name?").ask()
                password = questionary.password("What's your password?").ask()

                self.registration(name, password) 
                questionary.text("Registration was finished")
            elif command == "Update with csv":
                name = questionary.text("What's your name?").ask()
                password = questionary.password("What's your password?").ask()
                city = questionary.text("What's your city?").ask()
                age = questionary.text("What's your age?").ask()
                hobby = questionary.text("What's your hobby?").ask()
                self.update(name, password, city, age, hobby)
                questionary.text("Update was finished")

            elif command == "Get all users":
                self.get_users()

            elif command == "Get specific user":
                name = questionary.text("What's name?").ask()
                self.get_user(name)

    def registration(self, name: str, password: str):
        """
        Registers a new user.

        Sends a POST request to the registration endpoint with the provided name and password.

        :param name: The username for registration.
        :param password: The password for the new user.
        """
        url = "http://localhost:8080/registration"
        user_data = {
            "username": name,
            "password": password,
        }
        response = requests.post(url, json=user_data)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)

    def update(self, name: str, password: str, city: str, age: str, hobby: str):
        """
        Updates user data.

        Sends a POST request to the update endpoint with the provided user data.

        :param name: The username to update.
        :param password: The new password.
        :param city: The user's city.
        :param age: The user's age.
        :param hobby: The user's hobby.
        """
        url = f"http://localhost:8080/upload/{name}"
        data = {
            "data": f"Password,City,Age,Hobby\n{password},{city},{age},{hobby}"
        }
    
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)

    def get_users(self):
        """
        Retrieves all users.

        Sends a GET request to the endpoint for retrieving all users.
        """
        url = "http://localhost:8080/get-users"
        response = requests.get(url)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)

    def get_user(self, name: str):
        """
        Retrieves specific user information.

        Sends a GET request to the endpoint for retrieving user information by name.

        :param name: The username to retrieve information for.
        """
        url = f"http://localhost:8080/get_information/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)
            