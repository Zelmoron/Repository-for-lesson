import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'testing_mock')))

from fastapi import APIRouter, Query
from pydantic import BaseModel
from testing_mock.utils import parse_csv


class User(BaseModel):
    username: str
    password: str
    # city: Optional[str] = None
    # age: Optional[int] = None
    # hobby: Optional[str] = None


users = [{"Username": "Tom", "Password": "123", "City": "Irkutsk", "Age": "25", "Hobby": "Chess"}]  
new_user = {}

router = APIRouter()

@router.get("/upload/{username}")
def upload_user_data(username: str, data: str = Query(...)):
    user_data_list = parse_csv(data)
    
    for user_data in user_data_list:
        for user in users:
            if user.get("Username") == username:
                user["City"] = user_data.get("City")
                user["Age"] = user_data.get("Age")
                user["Hobby"] = user_data.get("Hobby")

                return {"message": users}
    
    return {"message": "Nothing changed"}


@router.post("/registration")
def registration(user: User):
    for existing_user in users:
        if existing_user["username"] == user.username:
            return {"message": "this user already exists"}

    new_user = {
        "username": user.username,
        "password": "f2ui190dwf" + user.password + "34254" + "!" * 4,
        "city": "",
        "age": 0,
        "hobby":""
    }

    users.append(new_user)

    return {
        "username": new_user["username"],
        "message": "registration successful"
    }
