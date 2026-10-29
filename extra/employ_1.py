import json
import csv

with open("salaries_1.csv","r",encoding="utf-8") as f:
    salary=csv.DictReader(f)
    salary_data={}
    for row in salary:
     salary_data[int(row["id"])]=int(row["salary"])
    # print(salary_data)

with open("employees_1.json","r",encoding="utf-8") as f:
   data=json.load(f)
   employee_count=0
   python_employees=0
   total_it_salary=0
   highest_salary=0
   high_earn=None
   for i in data['employees']:
        if i['department']=="IT":
         employee_count+=1
         if "Python" in i["skills"]:
           python_employees+=1
         total_salary=salary_data[i["id"]]
         total_it_salary+=total_salary
         if total_salary>highest_salary:
            highest_salary=total_salary
            high_earn=i["name"]
   average=round(total_it_salary/employee_count,2)
   
#    print(high_earn)
report = {
    "department": "IT",
    "employee_count": employee_count,
    "average_salary": average,
    "highest_paid": {
        "name":high_earn,
        "salary":highest_salary
    },
    "python_employees": python_employees
}

with open("report.json","w",encoding="utf-8") as f:
   json.dump(report,f,indent=4)