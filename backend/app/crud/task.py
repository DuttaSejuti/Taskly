from sqlalchemy.orm import Session
from app.models.task import Task
from app import schemas

def create_task(db: Session, task: schemas.TaskCreate):
  new_task = Task(**task.dict())
  db.add(new_task)
  db.commit()
  db.refresh(new_task)

  return new_task

def get_task(db: Session, task_id: int):
  return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 50):
  return db.query(Task).offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
  db_task = db.query(Task).filter(Task.id == task_id).first()
  if db_task:
    if task.title:
      db_task.title = task.title
    if task.description:
      db_task.description = task.description
    if task.is_completed is not None:
      db_task.is_completed = task.is_completed

  db.commit()
  db.refresh(db_task)

  return db_task
