import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# BBC main page ke Top Stories section ke liye naya selector
top_stories = soup.select("section h2")

headlines = []
for h in top_stories:
    text = h.get_text(strip=True)
    if text and "BBC" not in text and "Most" not in text and "Sport" not in text:
        headlines.append(text)

# Duplicate remove karna
headlines = list(dict.fromkeys(headlines))

with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(headlines, start=1):
        f.write(f"{i}. {line}\n")

print(f"✅ {len(headlines)} headlines 'headlines.txt' file me save ho gayi!")