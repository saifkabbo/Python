# import requests

# # url="https://jsonplaceholder.typicode.com/todos"
# url = "https://jsonplaceholder.typicode.com/does-not-exist"
# params={"userId":2}
# response=requests.get(url,params=params)
# # print(response.status_code)
# try: 
#  response.raise_for_status()
# except requests.exceptions.HTTPError:
#  print("HTTP request failed")
# data=response.json()
# print(data)
# # print(len(data))
# # count=0
# # False_count=0
# # for todo in data:
# #  if todo["completed"]==True:
# #   count+=1
# #  else:
# #   False_count+=1
# # print(count)

import requests
url = "https://jsonplaceholder.typicode.com/todos"
api_key=...
todo = {
    "title": "Learn APIs",
    "completed": False
}
headers = {
    "Content-Type": "application/json",
    "Authorization":f"Bearer {api_key}",
    "Accept":"application/json"
}
response=requests.post(url,json=todo,headers=headers)
created_todo=response.json()

print(created_todo)