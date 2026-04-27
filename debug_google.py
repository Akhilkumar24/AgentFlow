import requests
from bs4 import BeautifulSoup

def google_test(query):
    # Using a Mobile User-Agent to get simpler HTML
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    res = requests.get(url, headers=headers)
    print("Status:", res.status_code)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # In mobile view, links are often in <a> tags inside <div> with specific classes
    links = []
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if '/url?q=' in href and not 'google.com' in href:
            clean_url = href.split('/url?q=')[1].split('&')[0]
            links.append(clean_url)
    
    print("Links found:", len(links))
    for l in links[:3]:
        print("-", l)

google_test("EV India")
