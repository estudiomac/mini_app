from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.models import init_db
from backend.router.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Bot Is Ready")
    yield

app = FastAPI(title="Telegram Mini App", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")