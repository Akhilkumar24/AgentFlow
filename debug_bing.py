import requests
from bs4 import BeautifulSoup

def bing_test(query):
    url = f"https://www.bing.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    print("Status:", res.status_code)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # Bing links are in <h2> <a href="...">
    results = soup.find_all('li', class_='b_algo')
    print("Bing Results:", len(results))
    for r in results[:3]:
        a = r.find('a')
        if a:
            print("-", a.text, "|", a['href'])

bing_test("EV India")
