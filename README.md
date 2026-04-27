# Multi-Agent Platform

A modular, scalable multi-agent platform using Python and FastAPI. It includes Planner, Researcher, Writer, and Reviewer agents orchestrating a workflow to fulfill a user goal.

## Architecture
- **API Layer (`app/api/`)**: Built with FastAPI. Exposes endpoints to start tasks and check their status.
- **Orchestrator (`app/orchestrator/`)**: Manages the workflow (Planner -> Researcher -> Writer <-> Reviewer). Contains the feedback loop to retry the Writer if the Reviewer requests improvements.
- **Agents (`app/agents/`)**: Individual classes for each role, inheriting from a `BaseAgent` with built-in retry mechanisms using `tenacity`.
- **Tools (`app/tools/`)**: Modular functions (like search and summarize) that agents use. Keeps logic out of the agent classes directly.
- **Memory (`app/memory/`)**: A simple JSON-based storage for tracking task progress, intermediate states, and outputs across the system.

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the FastAPI server:
   ```bash
   python main.py
   ```
   Alternatively: `uvicorn main:app --reload`

3. Open the minimal frontend:
   Open `frontend/index.html` in your web browser.

4. Usage:
   - Enter a goal in the frontend, e.g., "Write a report on AI agents".
   - The frontend will poll the API and update the logs with the progress of the multi-agent system.
