from duckduckgo_search import DDGS

query = "ev markets in india statistics and market share"
with DDGS() as ddgs:
    try:
        results = list(ddgs.text(query + " english", region='us-en', max_results=3))
        print("Results length:", len(results))
        for res in results:
            print("Title:", res.get("title"))
    except Exception as e:
        print("DDG Error:", e)
