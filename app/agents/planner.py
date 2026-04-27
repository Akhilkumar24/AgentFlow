from app.agents.base import BaseAgent
from app.utils.domain_detector import DomainDetector

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Planner")

    def process(self, user_goal: str) -> dict:
        domain = DomainDetector.detect(user_goal)
        
        # Clean goal
        stop_words = {"tell", "me", "give", "show", "what", "is", "how", "about", "reports", "the", "an", "a", "and"}
        words = user_goal.lower().split()
        clean_goal = " ".join([w for w in words if w not in stop_words]).strip()
        
        if not clean_goal: clean_goal = user_goal

        # Rule 1: Concise queries (max 12 words), no 'goal:' prefix, semantically distinct
        tasks = [
            {"id": 1, "category": "market_share", "query": f"{clean_goal} top companies and market share percentage"},
            {"id": 2, "category": "market_size", "query": f"{clean_goal} total valuation USD and CAGR growth"},
            {"id": 3, "category": "trends", "query": f"{clean_goal} latest technology innovations and adoption"},
            {"id": 4, "category": "policies", "query": f"{clean_goal} government regulations and industry policies"}
        ]
        
        self.logger.info(f"Generated {len(tasks)} distinct tasks for domain: {domain.upper()}")
        return {"goal": user_goal, "domain": domain, "tasks": tasks}
