from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def create_task(db: Session, task: TaskCreate):
  new_task = Task(**task.dict())
  db.add(new_task)
  db.commit()
  db.refresh(new_task)

  return new_task

def get_task(db: Session, task_id: int):
  return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 50):
  return db.query(Task).offset(skip).limit(limit).all()
