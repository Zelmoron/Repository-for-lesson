# User Management API Documentation

This API provides endpoints for user management, including registration, data upload, and information retrieval.

## Base Models

### User
```python
class User(BaseModel):
    username: str
    password: str
```

### UserData
```python
class UserData(BaseModel):
    data: str
```

## Endpoints

### Registration
Create a new user account.

```
POST /registration
```

**Request Body**
```json
{
    "username": "string",
    "password": "string"
}
```

**Responses**
- `200 OK`: Registration successful
```json
{
    "Username": "string",
    "message": "registration successful"
}
```
- `400 Bad Request`: User already exists
```json
{
    "detail": "This user already exists"
}
```

### Upload User Data
Upload additional user information via CSV.

```
POST /upload/{username}
```

**Parameters**
- `username` (path): Username of the target user

**Request Body**
```json
{
    "data": "string" // CSV formatted data
}
```

**Responses**
- `200 OK`: Data updated successfully
```json
{
    "message": {
        "Username": "string",
        "Password": "string",
        "City": "string",
        "Age": "integer",
        "Hobby": "string"
    }
}
```
- `404 Not Found`: User not found or password incorrect

### Get User Information
Retrieve user information by username.

```
GET /get_information/{username}
```

**Parameters**
- `username` (path): Username to look up

**Responses**
- `200 OK`: User information retrieved successfully
```json
{
    "message": {
        "City": "string",
        "Age": "integer",
        "Hobby": "string"
    }
}
```
- `404 Not Found`: No information found for username

### Get All Users
Retrieve a list of all registered users.

```
GET /get-users
```

**Responses**
- `200 OK`: List of all users
```json
[
    {
        "Username": "string",
        "Password": "string",
        "City": "string",
        "Age": "integer",
        "Hobby": "string"
    }
]
```

## Data Structure
Users are stored with the following fields:
- `Username`: User's unique identifier
- `Password`: User's password
- `City`: User's city (optional)
- `Age`: User's age (optional)
- `Hobby`: User's hobby (optional)

## Error Handling
The API uses standard HTTP status codes for error handling:
- `400`: Bad Request - Usually indicates a validation error or duplicate user
- `404`: Not Found - Resource (user) not found
- `500`: Internal Server Error - Server-side error

## Dependencies
- FastAPI
- Pydantic
- Custom CSV parsing utility (`testing_mock.utils.parse_csv`)