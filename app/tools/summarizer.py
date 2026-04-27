from app.utils.logger import setup_logger
import re

logger = setup_logger("tools.summarizer")

def summarize_text(text: str) -> str:
    """Smart summarizer with minimum length validation."""
    if not text or len(text) < 100:
        logger.warning(f"Skipping summarization for invalid/short text (Length: {len(text) if text else 0})")
        return text if text else "No substantive content found."
    
    # Extract clean text from source markers
    clean_text = re.sub(r'Source:.*?\nData:', '', text, flags=re.DOTALL)
    
    # Simple logic for now: take first 400 chars but ensure it ends at a word
    if len(clean_text) > 400:
        summary = clean_text[:400].rsplit(' ', 1)[0] + "..."
        return summary
        
    return clean_text
