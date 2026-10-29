import requests
from bs4 import BeautifulSoup

url='https://archive.ics.uci.edu/dataset/45/heart+disease'
try:
    response=requests.get(url)
    response.raise_for_status()
    # print(response.status_code)
except requests.RequestException as e:
    print(f"Error: {e}")

soup=BeautifulSoup(response.text,"html.parser")

# print(soup.title.get_text(strip=True)if soup.title else "No title")
# print(len(soup.find_all("table")))
# print("Page headings:")
# for heading in soup.find_all(["h1", "h2", "h3"]):
#     print(heading.get_text(strip=True))


# for tag in soup.find_all(string=lambda text: text and "Heart Disease" in text):
#     print(tag.strip())

# print("Tables:", len(soup.find_all("table")))

# print(soup.title.get_text(strip=True))

# tables = soup.find_all("table")

# for i, table in enumerate(tables):
#     print(f"\nTable {i}:")
#     print(table.get_text(" ", strip=True)[:500])


import json

table = soup.find_all("table")[0]

headers = [th.get_text(strip=True) for th in table.find_all("th")]

rows = []

for tr in table.find_all("tr"):
    cells = tr.find_all("td")
    if cells:
        values = [cell.get_text(" ", strip=True) for cell in cells]
        rows.append(dict(zip(headers, values)))

with open("web_scraping/heart_disease.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=4, ensure_ascii=False)

print("JSON file saved!")