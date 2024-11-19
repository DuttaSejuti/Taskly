from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def create_task(db: Session, task: TaskCreate):
  new_task = Task(**task.dict())
  db.add(new_task)
  db.commit()
  db.refresh(new_task)

  return new_task
