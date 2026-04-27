from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.writer import WriterAgent
from app.agents.reviewer import ReviewerAgent
from app.utils.logger import setup_logger
import time

logger = setup_logger("orchestrator")

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()
        self.max_iterations = 3

    def run_task(self, goal: str):
        logger.info(f"--- STARTING PIPELINE: {goal} ---")
        
        # 1. PLAN
        plan = self.planner.process(goal)
        yield {"step": "PLANNER", "data": plan}

        # 2. ITERATIVE LOOP
        current_research = []
        feedback = None
        
        for i in range(self.max_iterations):
            logger.info(f"--- ITERATION {i+1} ---")
            
            # RESEARCH (Using plan or modified plan)
            current_research = self.researcher.process(plan)
            yield {"step": f"RESEARCHER_L{i+1}", "data": current_research}

            # WRITE
            report = self.writer.process({"goal": goal, "research": current_research, "feedback": feedback})
            yield {"step": f"WRITER_DRAFT_{i+1}", "data": report}

            # REVIEW
            review = self.reviewer.process(report)
            yield {"step": f"REVIEWER_FEEDBACK_{i+1}", "data": review}

            if review["status"] == "approved":
                yield {"step": "FINAL_REPORT", "data": report}
                return

            feedback = review["feedback"]
            logger.warning(f"REJECTED: {feedback}")
            
            # Smart Retry: Update planner tasks for next iteration
            for task in plan["tasks"]:
                task["query"] = f"latest {task['query']} statistics"
            
            time.sleep(1)

        yield {"step": "FINAL_REPORT", "data": report}
