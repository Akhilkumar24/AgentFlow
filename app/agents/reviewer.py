from app.agents.base import BaseAgent

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Reviewer")

    def process(self, report: dict) -> dict:
        if not report:
            return {"status": "needs_improvement", "feedback": "Report is empty."}
            
        sections = report.get("sections", [])
        
        # 1. ENFORCE MINIMUM 4 SECTIONS
        if len(sections) < 4:
            return {"status": "needs_improvement", "feedback": "Report must have exactly 4 sections."}

        # 2. ENFORCE SECTION LENGTH (Strictly split by whitespace)
        for s in sections:
            content_raw = s.get("content", "")
            word_count = len(content_raw.split()) # Strict whitespace split
            if word_count < 70:
                return {"status": "needs_improvement", "feedback": f"Section '{s['heading']}' is too short ({word_count} words). Minimum 70 required."}

        # 3. ENFORCE TOTAL LENGTH (Strictly split by whitespace)
        all_text = " ".join([s["content"] for s in sections])
        total_words = len(all_text.split())
        if total_words < 300:
            return {"status": "needs_improvement", "feedback": f"Report total length ({total_words} words) is under the 300-word minimum."}

        # 4. ENFORCE UNIQUENESS (No duplication)
        contents = [s["content"][:60] for s in sections]
        if len(set(contents)) < len(contents):
            return {"status": "needs_improvement", "feedback": "Duplicate content detected across sections."}

        return {"status": "approved", "feedback": "High-quality structured report approved."}
