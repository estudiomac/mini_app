from pydantic import BaseModel

class AddTask(BaseModel):
    title: str
    tg_id: int

class CompleteTask(BaseModel):
    id: int