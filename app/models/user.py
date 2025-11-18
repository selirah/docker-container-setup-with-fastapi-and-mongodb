from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime, timezone

class User(Document):
    user_id: str = Field(..., description="Unique ID for user")
    email: EmailStr = Field(..., description="User's email address")
    full_name: str = Field(..., description="User's full name")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"