from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": "I am happy",
    "age": 12,
}

data_without_age = {
    "email": "abc@mail.ru",
    "bio": "I am happy",
    # "gender": "male",
    # "birthday": "2022"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')

users = []

@app.post('/users/')
def add_user(user: UserSchema):
    users.append(user)
    return {"success": True,
            "message": "User added"}

@app.get('/users/')
def get_user():
    return users

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)




#
#
# print(UserSchema(**data_without_age))
# print(UserAgeSchema(**data))

