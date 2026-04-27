import requests
from bs4 import BeautifulSoup

url = "https://html.duckduckgo.com/html/"
data = {"q": "EV India"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://html.duckduckgo.com",
    "Referer": "https://html.duckduckgo.com/"
}

res = requests.post(url, headers=headers, data=data)
soup = BeautifulSoup(res.text, "html.parser")
results = soup.find_all('div', class_='result')
print("POST Results found:", len(results))

for r in results[:3]:
    a = r.find('a', class_='result__a')
    if a:
        print("-", a.text.strip(), "|", a['href'])
