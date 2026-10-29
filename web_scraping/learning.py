# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # url = 'https://example.com'
# # # # response=requests.get(url,timeout=10)
# # # # status=response.status_code

# # # # soup=BeautifulSoup(response.text,"html.parser")
# # # # # print(soup.title)
# # # # print(soup.p.get_text())

# # # from bs4 import BeautifulSoup

# # # html = """
# # # <html>
# # #     <body>
# # #         <h2>Python</h2>
# # #         <h2>JavaScript</h2>
# # #         <h2>Java</h2>
# # #     </body>
# # # </html>
# # # """

# # # soup = BeautifulSoup(html, "html.parser")

# # # first = soup.find("h2")
# # # print(first.get_text())

# # # all_headings = soup.find_all("h2")

# # # for heading in all_headings:
# # #     print(heading.get_text())

# # from bs4 import BeautifulSoup

# # html = """
# # <a href="https://www.python.org">Visit Python</a>
# # <a href="https://www.github.com">Visit GitHub</a>
# # """

# # soup = BeautifulSoup(html, "html.parser")

# # links = soup.find_all("a")

# # for link in links:
# #     print(link.get_text())
# #     print(link.get("href"))

# import requests
# import json
# from bs4 import BeautifulSoup

# url = "https://example.com"

# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")

#     title = soup.title.get_text(strip=True) if soup.title else None

#     data = {"url": url, "title": title}

#     with open("scraped_data.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4)

#     print(data)

# except requests.RequestException as e:
#     print("Request failed:", e)

# title = soup.title.get_text(strip=True) if soup.title else None

