import motor.motor_asyncio
from beanie import init_beanie

from app.models.user import User
from app.core.config import settings


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URI)
    await init_beanie(
        database=client.get_default_database(), # type: ignore[attr-defined]
        document_models=[User]
    )
