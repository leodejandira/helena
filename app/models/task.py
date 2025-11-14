from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: datetime
    priority: str = "medium"

class TaskResponse(TaskCreate):
    id: int
    created_at: datetime
    status: str