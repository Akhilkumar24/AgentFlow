import requests
from bs4 import BeautifulSoup

def news_test(query):
    # Google News RSS URL
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    res = requests.get(url)
    print("Status:", res.status_code)
    soup = BeautifulSoup(res.text, "xml") # Use XML parser
    
    items = soup.find_all('item')
    print("News items found:", len(items))
    for item in items[:3]:
        print("-", item.title.text, "|", item.link.text)

news_test("EV India")
