from fastapi import APIRouter, Depends
from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

from app.models.user import User


router = APIRouter(tags=["User"])

class UserResponse(BaseModel):
    id: str
    user_id: str
    email: EmailStr
    full_name: str
    created_at: datetime

class UserUpdate(BaseModel):
    full_name: Optional[str]

# GET /me
@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends()):
    return UserResponse(**user.model_dump(exclude={"id"}), id=str(user.id))


# PUT /me
@router.put("/me", response_model=UserResponse)
async def update_me(payload: UserUpdate, user: User = Depends()):
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    await user.save()
    return UserResponse(**user.model_dump(exclude={"id"}), id=str(user.id))