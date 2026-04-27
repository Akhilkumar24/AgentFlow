from app.agents.base import BaseAgent
from app.tools.search import mock_search
from app.tools.summarizer import summarize_text
from concurrent.futures import ThreadPoolExecutor

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def _execute_task(self, task):
        # Pass category to search tool
        raw_data = mock_search(task["query"], category=task.get("category", "general"))
        return {
            "task_id": task["id"],
            "query": task["query"],
            "category": task.get("category"),
            "raw_data": raw_data,
            "summary": summarize_text(raw_data)
        }

    def process(self, planner_output: dict) -> list:
        tasks = planner_output.get("tasks", [])
        with ThreadPoolExecutor(max_workers=4) as executor:
            return list(executor.map(self._execute_task, tasks))
