import requests
from bs4 import BeautifulSoup

url = "https://html.duckduckgo.com/html/?q=EV+India"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# Look for result divs
results = soup.find_all('div')
for r in results:
    if 'result' in r.get('class', []):
        print("Found result class:", r.get('class'))
        a = r.find('a', class_='result__a')
        if a:
            print("Link:", a['href'])

print("Total divs found:", len(results))
if len(results) < 50:
    print("HTML Snippet:", res.text[:500])
