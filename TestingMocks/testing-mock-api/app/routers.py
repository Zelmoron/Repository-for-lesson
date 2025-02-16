
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    # city: Optional[str] = None
    # age: Optional[int] = None
    # hobby: Optional[str] = None


router = APIRouter()
users = []  
new_user = {}
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