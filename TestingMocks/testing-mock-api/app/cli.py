
import questionary
import requests

class CLI:
    def __init__(self):
        pass

    def start_message(self):
        while True:
            command = questionary.select(
                "What do you want to do?",
                choices=["Registration", "Update with csv", "Get all users", "Get specific user"],
            ).ask()
            
            if command == "Registration":
                name = questionary.text("What's your name?").ask()
                password = questionary.password("What's your password?").ask()

                self.registration(name,password) 
                questionary.text("Registration was finished")
            if command == "Update with csv":
                name = questionary.text("What's your name?").ask()
                password = questionary.password("What's your password?").ask()
                city = questionary.text("What's your city?").ask()
                age = questionary.text("What's your age?").ask()
                hobby = questionary.text("What's your hobby?").ask()
                self.update(name,password,city,age,hobby)
                questionary.text("Update was finished")

            if command == "Get all users":
                self.get_users()

            if command == "Get specific user":
                name = questionary.text("What's name?").ask()
                self.get_user(name)

                


                

    def registration(self,name:str,password:str):
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


    def update(self,name:str,password:str,city:str,age:str,hobby:str):
        url = f"http://localhost:8080/upload/{name}?data=Password,City,Age,Hobby%0A{password},{city},{age},{hobby}"
        response = requests.get(url)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)

    def get_users(self):
        url = "http://localhost:8080/get-users"
        response = requests.get(url)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)
    def get_user(self,name:str):
        url = f"http://localhost:8080/get_information/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)
