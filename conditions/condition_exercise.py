# # age=int(input("Enter your age: "))
# # if age>=18:
# #     print("You are old enough to drive.")
# # else:
   
# #  print(f"You need {18-age} more years to learn to drive.")

# # my_age=22
# # your_age=int(input("Enter your age: "))
# # if my_age>your_age:
# #     print(f"I'm {my_age-your_age} years older than you")
# # elif my_age==your_age:
# #     print("We're both same age.")
# # else:
# #     print(f"You are {your_age-my_age} years older than me.")

# # a=int(input("Enter number one: "))
# # b=int(input("Enter number two:"))

# # if a>b:
# #     print(f"{a} is greater then {b}")
# # elif a==b:
# #     print(f"{a} and {b} are same.")
# # else:
# #     print(f"{b} is greater then {a}")

# # number=int(input("Enter your number: "))
# # if 90<= number <=100:
# #     print("Grade: A")
# # elif 80<= number <=89:
# #     print("Grade: B")
# # elif 70<= number <=79:
# #     print("Grade: C")
# # elif 60<= number <=69:
# #     print("Grade: D")
# # elif 00<= number <=59:
# #     print("Grade: F")
# # else:
# #     print("Number not more then 100 or less than 0.")

# # autumn=["september", "october" ,"november"]
# # winter=["december","january","febuary"]
# # spring=["march","april","may"]
# # summer=["june","july","august"]

# # user=input("Enter your month: ").lower().strip()

# # if user in autumn:
# #     print("It's Autumn")
# # elif user in winter:
# #     print("It's Winter")
# # elif user in spring:
# #     print("It's Spring")
# # elif user in summer:
# #     print("It's Summer")
# # else:
# #     print("Invalid!")

# # fruits = ['banana', 'orange', 'mango', 'lemon']

# # user=input("Enter the Fruits: ")

# # if user in fruits:
# #     print(f" '{user}' are already exist in the fruits list")
# # else:
# #     fruits.append(user)
# #     print(fruits)
# #     print(f"{user} added to this list.")

# person={
#     'first_name': 'Abu',
#     'last_name': 'Saif',
#     'age': 250,
#     'country': 'Bangladesh',
#     'is_married': False,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02200'
#     }
#     }

# # print('skills' in person)
# # print(person['skills'][round(len(person['skills'])/2)])

# # if "skills" in person:
# #     s=input("Enter the skills: ").capitalize().strip()
# #     if s in person["skills"]:
# #         print(f"The Person has {s} skill.")
# #     else:
# #         print(f"The person does not have {s} skill.")
# # else:
# #     print("The person has no skills key.")

# # skills = input("Enter skills: ").lower().split(",")
# # print(skills)
# # if "react" in skills and "node" in skills and "mongodb" in skills:
# #     print("He is a fullstack developer")

# # elif "javascript" in skills and "react" in skills:
# #     print("He is a front end developer")

# # elif "node" in skills and "python" in skills and "mongodb" in skills:
# #     print("He is a backend developer")

# # else:
# #     print("Unknown title")


# if person['is_married']==False and person['country']=='Bangladesh':
#     print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
# else:
#     print("Wrond Person!")