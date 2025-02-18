import sys
import os
from typing import List, Dict, Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'testing_mock')))

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from testing_mock.utils import parse_csv


class User(BaseModel):
    username: str
    password: str
    # city: Optional[str] = None
    # age: Optional[int] = None
    # hobby: Optional[str] = None


class UserData(BaseModel):
    data: str

users: List[Dict] = []
new_user: Dict = {}

router = APIRouter()

@router.post("/upload/{username}")
async def upload_user_data(username: str, user_data: UserData):
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
    for user in users:
        if user.get("Username") == username:
            data = {"City": user.get("City"), "Age": user.get("Age"), "Hobby": user.get("Hobby")}

            return {"message": data}

    raise HTTPException(status_code=404, detail="No information for this username")


@router.post("/registration")
async def registration(user: User):
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
    return users