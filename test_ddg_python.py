from duckduckgo_search import DDGS

try:
    with DDGS() as ddgs:
        # Trying a super common query to see if anything comes back
        results = list(ddgs.text("python", max_results=3))
        print("Results for 'python':", len(results))
except Exception as e:
    print("Error:", e)
