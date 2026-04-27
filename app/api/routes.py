import uuid
from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.api.schema import TaskRequest, TaskResponse, TaskStatusResponse
from app.orchestrator.workflow import Orchestrator
from app.memory.storage import memory_store

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/run-task", response_model=TaskResponse)
async def run_task(request: TaskRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    memory_store.save(task_id, {"status": "pending", "goal": request.goal})
    
    background_tasks.add_task(orchestrator.run_workflow, task_id, request.goal)
    
    return TaskResponse(task_id=task_id, message="Task started in the background.")

@router.get("/status/{task_id}", response_model=TaskStatusResponse)
async def get_status(task_id: str):
    data = memory_store.load(task_id)
    if not data:
        raise HTTPException(status_code=404, detail="Task not found")
        
    return TaskStatusResponse(
        task_id=task_id,
        status=data.get("status", "unknown"),
        data=data
    )
