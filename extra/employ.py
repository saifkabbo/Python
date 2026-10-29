# import csv
# with open("employ.csv","r",encoding="utf-8") as f:
#     missing_salary=0
#     highest_salary=0
#     top_earn=None
#     for row in csv.DictReader(f):
#         if row["salary"]=="":
#          missing_salary+=1
#         elif int(row["salary"])>highest_salary:
#             highest_salary=int(row["salary"])
#             top_earn=row["name"]
#     print(f"Missing salary: {missing_salary}\nHighest salary: {top_earn} = {highest_salary}")


text = '''
{
    "employees": [
        {"name": "Alice", "salary": 60000},
        {"name": "Bob", "salary": 45000},
        {"name": "Charlie", "salary": 75000}
    ]
}
'''

import json

text=json.loads(text)
dictionary=text["employees"]
top_salary=0
top_earn=None
for i in range(len(dictionary)):
    if int(text["employees"][i]["salary"])>top_salary:
        top_salary=int(text["employees"][i]["salary"])
        top_earn=text["employees"][i]["name"]
    
result={
    "name":top_earn,
    "salary":top_salary
}


print(json.dumps(result,indent=4))

