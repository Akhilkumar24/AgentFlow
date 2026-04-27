# 📑 Multi-Agent Report Generation System

> **An automated, modular, and scalable AI-driven pipeline that orchestrates specialized agents to transform high-level prompts into comprehensive, data-driven analytical reports.**

---

## 📝 Overview
The **Multi-Agent Report Generation System** is a sophisticated Python-based framework designed to solve the complexity of long-form content creation. Unlike standard LLM prompts that often suffer from hallucination or lack of depth, this system employs a **distributed agentic workflow**. 

By decoupling the process into specialized roles—**Planning, Research, Writing, and Reviewing**—the system ensures high accuracy, structural integrity, and professional-grade output. The architecture leverages JSON-based inter-agent communication, persistent memory, and comprehensive logging to create a production-ready automation tool.

---

## 🚀 Key Features
* **Agentic Orchestration:** Specialized agents with distinct personas and constraints.
* **Modular Architecture:** Highly decoupled components allowing for easy scaling or agent swapping.
* **Stateful Memory:** Maintains context across the generation lifecycle for coherent long-form reports.
* **Structured Communication:** Uses standardized JSON schemas for seamless data exchange between agents.
* **Automated Quality Assurance:** Built-in Reviewer agent to enforce consistency and factual correctness.
* **Extensive Logging:** Detailed execution traces for debugging and performance monitoring.

---

## 🏗 System Architecture
The system follows a **sequential and iterative multi-agent design**, where the output of one agent serves as the validated input for the next.

### 🧩 The Agents
1.  **The Planner:** Acts as the project manager. It analyzes the user’s high-level intent and decomposes it into a structured execution plan (To-Do lists, outlines, and key objectives).
2.  **The Researcher:** The data engine. It processes complex information, extracts relevant facts, and synthesizes data points required for the report.
3.  **The Writer:** The creative engine. Using the research synthesis and the plan, it drafts a structured, professional report following Markdown best practices.
4.  **The Reviewer:** The gatekeeper. It audits the draft against the original plan, checking for tone, technical accuracy, and formatting consistency.

---

## 🔄 Workflow
1.  **Input Ingestion:** The user provides a high-level topic or research prompt.
2.  **Task Decomposition:** The **Planner** generates a detailed JSON-based roadmap.
3.  **Knowledge Synthesis:** The **Researcher** executes data gathering based on the roadmap.
4.  **Draft Generation:** The **Writer** consumes the research context to produce a structured document.
5.  **Audit & Refine:** The **Reviewer** validates the document. If it fails quality checks, it is sent back for revision.
6.  **Final Output:** A polished, ready-to-deploy analytical report.

---

## 🛠 Tech Stack
* **Language:** Python 3.9+
* **AI Orchestration:** [e.g., LangChain / CrewAI / Custom Framework]
* **Data Handling:** JSON, Pydantic (for schema validation)
* **Logging:** Python Logging Module
* **Environment:** Dotenv for secure API management
* **Deployment:** Render

---

## 📁 Project Structure

multi-agent-report-gen/
├── agents/
│   ├── planner.py       # Task decomposition logic
│   ├── researcher.py    # Information gathering & processing
│   ├── writer.py        # Content generation logic
│   └── reviewer.py      # Quality assurance & validation
├── core/
│   ├── memory.py        # Context persistence
│   ├── logger.py        # Execution tracking
│   └── utils.py         # Helper functions
├── logs/                # Execution traces
├── reports/             # Generated output files
├── .env.example         # Environment variable template
├── app.py               # Main entry point
├── requirements.txt     # Dependencies
└── README.md            # Documentation

## ⚙️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/multi-agent-report-gen.git](https://github.com/your-username/multi-agent-report-gen.git)
    cd multi-agent-report-gen
    ```

2.  **Create Virtual Environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate it (MacOS/Linux)
    source venv/bin/activate  

    # Activate it (Windows)
    # venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**
    Create a `.env` file in the root directory and add your credentials:
    ```text
    OPENAI_API_KEY=your_api_key_here
    LOG_LEVEL=INFO
    REPORT_OUTPUT_DIR=./reports
    ```

5.  **Run the Application:**
    ```bash
    python app.py
    ```

---

## 🌐 Deployment (Render)

This project is optimized for deployment on **Render** as a Background Worker or Web Service.

1.  **Connect GitHub:** Link your repository to the Render Dashboard.
2.  **Service Type:** Select **Python** as the runtime.
3.  **Build Command:** ```bash
    pip install -r requirements.txt
    ```
4.  **Start Command:** ```bash
    python app.py
    ```
5.  **Environment Variables:** Add your `.env` keys (like `OPENAI_API_KEY`) in the Render "Environment" tab to ensure secure execution.
