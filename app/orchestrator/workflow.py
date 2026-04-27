import uuid
from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.writer import WriterAgent
from app.agents.reviewer import ReviewerAgent
from app.memory.storage import memory_store
from app.utils.logger import setup_logger
from app.config import config

logger = setup_logger("orchestrator")

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def run_workflow(self, task_id: str, goal: str):
        logger.info(f"Starting workflow for task {task_id}: {goal}")
        memory_store.save(task_id, {"status": "running", "goal": goal, "steps": []})
        
        try:
            plan = self.planner.run(goal)
            self._update_memory(task_id, "planner", plan)
            
            research = self.researcher.run(plan)
            self._update_memory(task_id, "researcher", research)
            
            loop_count = 0
            feedback = None
            final_report = None
            
            while loop_count < config.MAX_WORKFLOW_LOOPS:
                loop_count += 1
                logger.info(f"Drafting report, attempt {loop_count}")
                
                writer_input = {
                    "goal": goal,
                    "research": research,
                    "feedback": feedback
                }
                
                draft = self.writer.run(writer_input)
                self._update_memory(task_id, f"writer_draft_{loop_count}", draft)
                
                review_result = self.reviewer.run(draft)
                self._update_memory(task_id, f"reviewer_feedback_{loop_count}", review_result)
                
                if review_result.get("status") == "approved":
                    final_report = draft
                    break
                else:
                    feedback = review_result.get("feedback")
                    
            if not final_report:
                logger.warning(f"Task {task_id} hit max workflow loops. Using latest draft.")
                final_report = draft
                
            self._update_memory(task_id, "final_report", final_report)
            
            memory_data = memory_store.load(task_id)
            memory_data["status"] = "completed"
            memory_store.save(task_id, memory_data)
            logger.info(f"Workflow completed for task {task_id}")
            
        except Exception as e:
            logger.error(f"Workflow failed for task {task_id}: {str(e)}")
            memory_data = memory_store.load(task_id)
            if memory_data:
                memory_data["status"] = "failed"
                memory_data["error"] = str(e)
                memory_store.save(task_id, memory_data)

    def _update_memory(self, task_id: str, step_name: str, data: dict):
        memory_data = memory_store.load(task_id)
        if memory_data:
            memory_data["steps"].append({"step": step_name, "data": data})
            memory_store.save(task_id, memory_data)
