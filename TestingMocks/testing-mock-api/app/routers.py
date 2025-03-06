import sys
import os
from typing import List, Dict, Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'testing_mock')))

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from testing_mock.utils import parse_csv

class User(BaseModel):
    """
    Model for user registration data.

    Attributes:
        username (str): The username chosen by the user.
        password (str): The password chosen by the user.
    """
    username: str
    password: str
    # city: Optional[str] = None
    # age: Optional[int] = None
    # hobby: Optional[str] = None

class UserData(BaseModel):
    """
    Model for user data uploaded in CSV format.

    Attributes:
        data (str): CSV data as a string.
    """
    data: str

# List to store user data
users: List[Dict] = []
# Dictionary to store new user data (not used in this code snippet)
new_user: Dict = {}

# Create a FastAPI router for handling user-related endpoints
router = APIRouter()

@router.post("/upload/{username}")
async def upload_user_data(username: str, user_data: UserData):
    """
    Uploads user data from a CSV string.

    Updates the user's city, age, and hobby if the username and password match.

    Args:
        username (str): The username to update.
        user_data (UserData): CSV data containing user information.

    Returns:
        dict: Updated user data if successful.

    Raises:
        HTTPException: If the user is not found or the password is incorrect.
    """
    user_data_list = parse_csv(user_data.data)

    for data in user_data_list:
        for user in users:
            if user.get("Username") == username and data.get("Password") == user["Password"]:
                user["City"] = data.get("City")
                user["Age"] = data.get("Age")
                user["Hobby"] = data.get("Hobby")

                return {"message": user}

    raise HTTPException(status_code=404, detail="User not found or password incorrect")


@router.get("/get_information/{username}")
async def get_information(username: str):
    """
    Retrieves user information by username.

    Returns city, age, and hobby for the specified user.

    Args:
        username (str): The username to retrieve information for.

    Returns:
        dict: User information if found.

    Raises:
        HTTPException: If no information is found for the username.
    """
    for user in users:
        if user.get("Username") == username:
            data = {"City": user.get("City"), "Age": user.get("Age"), "Hobby": user.get("Hobby")}

            return {"message": data}

    raise HTTPException(status_code=404, detail="No information for this username")


@router.post("/registration")
async def registration(user: User):
    """
    Registers a new user.

    Checks if the username already exists and creates a new user entry if not.

    Args:
        user (User): User registration data.

    Returns:
        dict: Registration success message with the new username.

    Raises:
        HTTPException: If the username already exists.
    """
    for existing_user in users:
        if existing_user["Username"] == user.username:
            raise HTTPException(status_code=400, detail="This user already exists")

    new_user = {
        "Username": user.username,
        "Password": user.password,
        "City": "",
        "Age": 0,
        "Hobby": ""
    }

    users.append(new_user)

    return {
        "Username": new_user["Username"],
        "message": "registration successful"
    }


@router.get("/get-users")
async def get_users():
    """
    Retrieves a list of all registered users.

    Returns:
        list: List of user dictionaries.
    """
    return users
