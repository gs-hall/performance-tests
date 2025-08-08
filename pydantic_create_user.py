from pydantic import BaseModel, Field, EmailStr

# UserSchema example

# Example structure for a user
# {
#   "id": "string",
#   "email": "string"
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"
# }

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str = Field(..., regex=r'^\+?[1-9]\d{1,14}$')

# CreateUserRequestSchema example
# {
#   "email": "string",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"
# }

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания нового пользователя.
    """
    # Используем EmailStr для валидации email
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str = Field(..., regex=r'^\+?[1-9]\d{1,14}$')

# CreateUserResponseSchema example
# {
# "user": {
#   "id": "string",
#   "email": "
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"
#   }
# }

class CreateUserResponseSchema(BaseModel):
    user: UserSchema