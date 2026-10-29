import requests
import json
url='http://www.bu.edu/president/boston-university-facts-stats/'

from bs4 import BeautifulSoup

try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    # print(response.status_code)
except requests.RequestException as e:
    print(e)

soup=BeautifulSoup(response.text,"html.parser")

# print(soap.get_text(" ",strip=True)[:2000])
# print(soup.find_all("h2"))
element = soup.find(string=lambda text: text and "Research Expenditures" in text)
container=element.parent.parent
label=container.find("h3",class_="bu-stat-title")
value=container.find("span",class_="bu-stat-value")
# print(label.get_text(strip=True))
# print(value.get_text(strip=True))
stat_containers = soup.find_all("div", class_="bu-stat-inner")

print("Total containers:", len(stat_containers))

stats=[]
for container in stat_containers:
    label_tag = container.find("h3", class_="bu-stat-title")
    label=label_tag.get_text(strip=True)
    value_tag = container.find("span", class_="bu-stat-value")
    value=value_tag.get_text(strip=True)
    prefix_tag = container.find("span",class_="bu-stat-prefix")
    suffix_tag = container.find("span",class_="bu-stat-suffix")
    prefix=prefix_tag.get_text(strip=True) if prefix_tag else ""
    suffix=suffix_tag.get_text(strip=True) if suffix_tag else ""

    if label_tag and value_tag:
        stats.append({'label':label,'value':f'{prefix}{value}{suffix}'})
# print(stats)

with open("web_scraping/data.json","w",encoding="utf-8") as f:
    json.dump(stats,f,indent=4)
