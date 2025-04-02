import backend.db.requests as rq

class TaskService:
    @staticmethod
    async def get_or_create_user(tg_id: int):
        return await rq.add_user(tg_id)

    @staticmethod
    async def get_tasks_for_user(user_id: int):
        return await rq.get_tasks(user_id)

    @staticmethod
    async def get_completed_count(user_id: int):
        return await rq.get_completed_tasks_count(user_id)

    @staticmethod
    async def add_task(user_id: int, title: str):
        await rq.add_task(user_id, title)

    @staticmethod
    async def complete_task(task_id: int):
        await rq.update_task(task_id)