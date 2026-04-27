import requests
from bs4 import BeautifulSoup

def search_lite(query):
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        print("Status code:", response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all('div', class_='result')
        print("Results found:", len(results))
        for r in results[:3]:
            title = r.find('a', class_='result__a')
            if title:
                print("-", title.text.strip())
    except Exception as e:
        print("Error:", e)

search_lite("EV India market")
