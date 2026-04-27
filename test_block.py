import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = "https://www.google.com/search?q=EV+market+in+India&hl=en"
res = requests.get(url, headers=headers)
with open("google_dump.html", "w", encoding="utf-8") as f:
    f.write(res.text)
