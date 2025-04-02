from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models.models import init_db
import backend.db.requests as rq
class AddTask(BaseModel):
    title: str
    tg_id: int

class completeTask(BaseModel):
    id: int

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

@app.get("/api/tasks/{tg_id}")
async def tasks(tg_id: int):
   user = await rq.add_user(tg_id)
   return await rq.get_tasks(user.id)

@app.get("/api/main/{tg_id}")
async def profile(tg_id: int):
    user = await rq.add_user(tg_id)
    completed_tasks_count = await rq.get_completed_tasks_count(user.id)
    return {'completed tasks': completed_tasks_count}

@app.post("/api/add")
async def add_task(task: AddTask):
    user = await rq.add_user(task.tg_id)
    await rq.add_task(user.id, task.title)
    return {'status': 'ok'}

@app.patch("/api/completed")
async def complete_task(task: completeTask):
    await rq.update_task(task.id)
    return {'status': 'ok'}