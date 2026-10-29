import json
import csv

with open("salaries.csv","r",encoding="utf-8") as f:
    salaries=csv.DictReader(f)
    salary_data={}
    for row in salaries:
     salary_data[row["id"]]=int(row["salary"])
    # print(salary_data)

with open("employees.json","r",encoding="utf-8") as f:
   data=json.load(f)
   highest_salary=0
   top_earn=None
   for employee in data["employees"]:
      if "Python" in employee["skills"]:
       salary=salary_data[str(employee["id"])]
    #    print(employee["name"],salary)
      if salary>highest_salary:
         highest_salary=salary
         top_earn=employee
#    print(f"Highest Earn: {top_earn} = ${highest_salary}")


top_earn["salary"]=highest_salary
# print(top_earn)

with open("top_employees.json","w",encoding="utf-8")as f:
   json.dump(top_earn,f,indent=4)