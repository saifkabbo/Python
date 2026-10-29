
import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

request_headers = {
    "User-Agent": "MyPythonLearningProject/1.0 (educational project)"
}

try:
    response = requests.get(url, headers=request_headers, timeout=15)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Request failed: {e}")
    raise SystemExit(1)

soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table")

# Select the presidents table

rows = tables.find_all("tr")

# Extract headers
headers = [
    cell.get_text(" ", strip=True)
    for cell in rows[0].find_all(["th", "td"], recursive=False)
]

data = []

# Process ALL remaining rows, not just the first one
for tr in rows[1:]:
    cells = tr.find_all(["th", "td"], recursive=False)

    values = [
        cell.get_text(" ", strip=True)
        for cell in cells
    ]

    row = dict(zip(headers, values))
    data.append(row)

# Save every extracted row
# with open("web_scraping/presidents.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)

# print("Total rows extracted:", len(data))
# print("All extracted records:")
# print(json.dumps(data, indent=4, ensure_ascii=False))