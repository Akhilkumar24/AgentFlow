import re

class DomainDetector:
    @staticmethod
    def detect(user_goal: str) -> str:
        goal = user_goal.lower()
        
        domains = {
            "ev": [r"ev", r"electric vehicle", r"tesla", r"charging", r"battery"],
            "finance": [r"finance", r"market", r"stock", r"economy", r"investment", r"bank"],
            "blockchain": [r"blockchain", r"crypto", r"bitcoin", r"ethereum", r"nft", r"defi"],
            "energy": [r"energy", r"solar", r"wind", r"power", r"renewable", r"grid"],
            "tech": [r"ai", r"software", r"cloud", r"semiconductor", r"hardware"]
        }
        
        for domain, patterns in domains.items():
            if any(re.search(p, goal) for p in patterns):
                return domain
                
        return "general"
