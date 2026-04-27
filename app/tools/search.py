from app.utils.logger import setup_logger
import requests
from bs4 import BeautifulSoup
from app.utils.knowledge_base import DomainKnowledge
from app.utils.domain_detector import DomainDetector

logger = setup_logger("tools.search")

def mock_search(query: str, category: str = "general", max_results: int = 1) -> str:
    """Search with Category-Specific Fallback (Domain Knowledge Mode)."""
    logger.info(f"--- [SEARCH_EXEC] Category: {category} | Query: '{query}' ---")
    
    domain = DomainDetector.detect(query)
    formatted = ""

    # 1. LIVE SEARCH
    try:
        url = f"https://html.duckduckgo.com/html/?q={query}"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.find_all('div', class_='result')
        if results:
            snippet = results[0].find('a', class_='result__snippet').text.strip()
            formatted += f"Source: Web\nData: {snippet}\n\n"
    except: pass

    # 2. DOMAIN KNOWLEDGE MODE (Guaranteed distinct fallback data)
    if not formatted:
        logger.warning(f"--- [KNOWLEDGE_MODE] Category: {category} ---")
        formatted += f"Source: Domain Insight ({category})\nData: {DomainKnowledge.get(domain, category)}\n\n"
        
    return formatted
