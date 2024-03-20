import re
from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    username: str
    email: EmailStr


class UserOut(User):
    id: int
    is_active: bool


class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    password: str
    confirm_password: str

    @validator("password", pre=True)
    def validate_password(cls, value):
        # Password should be at least 8 characters long and contain at least one uppercase, one lowercase, and one digit
        if not re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$",
            value,
        ):
            raise ValueError("Invalid password format")
        return value

    @validator("confirm_password")
    def validate_confirm_password(cls, value, values):
        # Confirm password should match the original password
        if "password" in values and value != values["password"]:
            raise ValueError("Passwords do not match")
        return value
