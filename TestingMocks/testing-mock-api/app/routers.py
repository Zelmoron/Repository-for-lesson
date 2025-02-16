from fastapi import APIRouter, Query
from pydantic import BaseModel
import csv



class User(BaseModel):
    username: str
    password: str
    # city: Optional[str] = None
    # age: Optional[int] = None
    # hobby: Optional[str] = None

#Временное решение, пока не натсроили нормальный импорт из utils
def parse_csv(csv_string: str) -> list[dict[str, str]]:
    data = []
    lines = csv_string.strip().split("\n")
    if not lines:
        return data

    reader = csv.DictReader(lines)
    for row in reader:
        data.append(row)
        
    return data

full_data: list[dict[str, str]] = []


users = []  
new_user = {}

router = APIRouter()

@router.get("/upload/{username}")
def upload_user_data(username: str, data: str = Query(...)):
    user_data_list = parse_csv(data)
    
    for user_data in user_data_list:
        full_data.append({
            "Username": username,
            "Password": user_data.get("Password"),
            "City": user_data.get("City"),
            "Age": user_data.get("Age"),
            "Hobby": user_data.get("Hobby")
        })
    
    return {"message": full_data}


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
