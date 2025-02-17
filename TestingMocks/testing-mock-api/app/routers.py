from fastapi import APIRouter, Query
from pydantic import BaseModel

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