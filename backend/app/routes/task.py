from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
  new_task = crud.create_task(db, task)

  return new_task

@router.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
  tasks = crud.get_tasks(db, skip, limit)

  return tasks

@router.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
  task = crud.get_task(db, task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")

  return task

@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
  db_task = crud.get_task(db, task_id)
  if not db_task:
    raise HTTPException(
        status_code=404,
        detail="Task doesn't exist and cannot be updated"
      )
  updated_task = crud.update_task(db, task_id, task)

  return updated_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
  db_task = crud.get_task(db, task_id)
  if not db_task:
    raise HTTPException(
        status_code=404, 
        detail="Task doesn't exist and cannot be deleted"
      )
  crud.delete_task(db, task_id)

  return {"detail": "Task has been successfully deleted"}
