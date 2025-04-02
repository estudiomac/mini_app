from fastapi import APIRouter
from backend.schemas.task import AddTask, CompleteTask
from backend.services.task_service import TaskService

router = APIRouter()

@router.get("/tasks/{tg_id}")
async def tasks(tg_id: int):
    user = await TaskService.get_or_create_user(tg_id)
    return await TaskService.get_tasks_for_user(user.id)

@router.get("/main/{tg_id}")
async def profile(tg_id: int):
    user = await TaskService.get_or_create_user(tg_id)
    count = await TaskService.get_completed_count(user.id)
    return {"completed tasks": count}

@router.post("/add")
async def add_task(task: AddTask):
    user = await TaskService.get_or_create_user(task.tg_id)
    await TaskService.add_task(user.id, task.title)
    return {"status": "ok"}

@router.patch("/completed")
async def complete_task(task: CompleteTask):
    await TaskService.complete_task(task.id)
    return {"status": "ok"}