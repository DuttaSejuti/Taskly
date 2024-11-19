from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
  title: Optional[str] = None
  description: Optional[str] = None
  is_completed: Optional[bool] = False

  class Config:
    orm_mode = True

class TaskCreate(TaskBase):
  title: str

class TaskResponse(TaskBase):
  id: int
