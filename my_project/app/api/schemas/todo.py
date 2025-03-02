import datetime

from pydantic import BaseModel


class ToDoCreate(BaseModel):
    description: str
    completed: bool | None = False


class ToDoFromDB(ToDoCreate):  # будем возвращать из БД - унаследовались от создания и расширили 2 полями
    id: int
    created_at: datetime.datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.todo import ToDoFromDB, ToDoCreate
from app.db.database import get_async_session
from app.db.models import ToDo

todo_router = APIRouter(
    prefix="/todo",
    tags=["ToDo"]
)


@todo_router.get("/", response_model=list[ToDoFromDB])
async def get_todos(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ToDo))
    return result.scalars().all()


@todo_router.post("/", response_model=ToDoFromDB)
async def create_todo(todo: ToDoCreate, session: AsyncSession = Depends(get_async_session)):
    new_todo = ToDo(**todo.model_dump())
    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)
    return new_todo
