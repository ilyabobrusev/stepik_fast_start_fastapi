from pydantic import BaseModel, EmailStr, conint

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: conint(gt=0) # type: ignore
    is_subscribed: bool = False
