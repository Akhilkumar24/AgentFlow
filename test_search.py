from googlesearch import search
try:
    results = list(search("EV market in India", num_results=3, advanced=True))
    for res in results:
        print("Title:", res.title)
        print("Desc:", res.description)
except Exception as e:
    print("Error:", e)

print("Standard search:")
try:
    for url in search("EV market in India", num_results=3):
        print(url)
except Exception as e:
    print("Error:", e)
