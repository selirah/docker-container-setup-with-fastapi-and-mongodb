from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db import init_db
import logging
from app.api.routes import user

@asynccontextmanager
async def lifespan(_app: FastAPI):
    logging.info("🌱 Initializing DB connection...")
    await init_db()
    logging.info("✅ DB initialized")
    yield
    logging.info("🧹 Cleaning up app (if needed)")

app = FastAPI(
    title="Test API",
    version="0.1.0",
    docs_url="/docs",
    lifespan=lifespan
)
@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Backend is alive 🚀"}

app.include_router(user.router)