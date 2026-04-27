from pydantic import BaseModel
from typing import Optional, Dict, Any

class TaskRequest(BaseModel):
    goal: str

class TaskResponse(BaseModel):
    task_id: str
    message: str
    
class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    data: Optional[Dict[str, Any]] = None
