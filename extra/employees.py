with open("employees.csv","r",encoding="utf-8") as f:
    next(f)
    count_age=0
    count_salary=0
    highest_salary=0
    top_earner=None
    for line in f:
     line=line.strip()
     name,age,salary=line.split(",")
     if age =="":
        count_age+=1
     if salary=="":
        count_salary+=1
     elif int(salary)>highest_salary:
        highest_salary=int(salary)
        top_earner=name
    
    print(f"Missing ages: {count_age}\nMissing salaries: {count_salary}\nHighest salary: {top_earner} = {highest_salary}")