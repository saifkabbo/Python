import requests
url="https://jsonplaceholder.typicode.com/todos"

x=int(input("Enter user ID: "))
params={"userId":x}

try:
    response=requests.get(url,params=params)
    response.raise_for_status()
    data=response.json()
except requests.exceptions.HTTPError:
    print("Request failed.")
else:
    if  len(data)==0:
     print("No todos found for this user")
    else:
        completed_count=0
        incompleted_count=0
        for todo in data:
            if todo["completed"]==True:
                completed_count+=1
            else:
                incompleted_count+=1
        print(f"Completed: {completed_count}\nIncomplete: {incompleted_count}")
