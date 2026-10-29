import json
import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
headers={
    'User-Agent':'MyPythonLearningProject/1.0'
}
try:
 response=requests.get(url,headers=headers)
#  print(response.status_code)
 response.raise_for_status()
 soup=BeautifulSoup(response.text,"html.parser")
except requests.RequestException as e:
 print(f"Error: {e}")
 exit()

span_text=soup.find_all('span',class_='text')
span_author=soup.find_all('small',class_='author')

# for tag in tags:
#  print(tag.get_text(' ',strip=True))

quotes=[item.get_text(" ",strip=True) for item in span_text]
authors=[item_1.get_text(" ",strip=True) for item_1 in span_author]

result = []
quote_blocks = soup.find_all("div", class_="quote")

for quote_block in quote_blocks:
    quote = quote_block.find("span", class_="text").get_text(" ", strip=True)
    author = quote_block.find("small", class_="author").get_text(" ", strip=True)
    tags = [
        tag.get_text(" ", strip=True)
        for tag in quote_block.find_all("a", class_="tag")
    ]
    result.append({
        "quote": quote,
        "author": author,
        "tags": tags
    })


with open("web_scraping/quote_author.json",'w',encoding="utf-8") as f:
  json.dump(result,f,ensure_ascii=False,indent=4)

