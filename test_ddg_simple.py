from duckduckgo_search import DDGS

try:
    with DDGS() as ddgs:
        results = list(ddgs.text("EV India", max_results=3))
        print("Results found:", len(results))
        for r in results:
            print("-", r['title'])
except Exception as e:
    print("Error:", e)
