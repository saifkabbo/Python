names = ["Saif", "Ali", "John"]
ages = [20, 30, 25]
countries = ["Bangladesh", "India", "USA"]

def create_people():
    people=[]
    for name,age,country in zip(names,ages,countries):
     person={"name": name,"age": age,"country": country}
     people.append(person)
    print(people)

create_people()