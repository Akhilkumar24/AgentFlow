import re

class DataValidator:
    @staticmethod
    def is_valid_search_result(text: str, min_length: int = 50) -> bool:
        """Relaxed validation to ensure we don't block useful data."""
        if not text or len(text) < min_length:
            return False
        # Only reject if it's explicitly an error message
        if "search failed" in text.lower():
            return False
        return True

    @staticmethod
    def clean_ascii(text: str) -> str:
        """Removes non-ascii and excessive whitespace."""
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        return " ".join(text.split()).strip()

    @staticmethod
    def check_diversity(sections: list) -> bool:
        """Lenient diversity check."""
        if len(sections) < 2: return True
        contents = [s.get("content", "")[:50] for s in sections]
        return len(set(contents)) >= (len(contents) * 0.7) # Allow some similarity
