# students = [
#     {"name": "Alice", "age": 20, "skills": {"Python", "SQL"}},
#     {"name": "Bob", "age": 22, "skills": {"Python", "Java"}},
#     {"name": "Charlie", "age": 21, "skills": {"Java", "C++"}}
# ]

# # print(students[0]["name"])
# # print(students[1]["skills"])
# # add_alice_skills=students[0]["skills"]
# # add_alice_skills.add("C++")
# # alice_skills=students[0]["skills"]
# # bob_sills=students[1]["skills"]
# # # print(alice_skills&bob_sills)
# # charlie_skills=students[2]["skills"]

# # print(alice_skills|bob_sills|charlie_skills)

# # if "Python" in students[0]["skills"]:
# #     print(students[0]["name"])

# # if "Python" in students[1]["skills"]:
# #     print(students[1]["name"])

# # if "Python" in students[2]["skills"]:
# #     print(students[2]["name"])

# # if "Python" in students[0]["skills"]:
# #     print(students[0]["name"])
# # print("Python" in students[1]["skills"])
# # print("Python" in students[2]["skills"])

# numbers = [1, 2, 2, 3, 4, 4, 5, 5]

# numbers=set(numbers)
# print(sum(numbers))

# python_students = {"Alice", "Bob", "David"}
# java_students = {"Bob", "Charlie", "David"}

# # print(python_students&java_students)

# # print((python_students|java_students)-(python_students^java_students))

# student = {
#     "name": "John",
#     "age": 21,
#     "skills": {"Python", "SQL"}
# }

# # print(student["name"])
# student["skills"].add("Java")

# print("Python" in student["skills"])

# students = [
#     {"name": "Alice", "age": 20},
#     {"name": "Bob", "age": 22},
#     {"name": "Charlie", "age": 21}
# ]

# # print(students[1]["name"])
# # print(students[2]["name"])
# students[0]["age"]=21
# students[2]["age"]=21
# print(students[0]["age"])

# A = {"Python", "SQL", "Java"}
# B = {"Python", "C++", "JavaScript"}

# all unique skills
# print(A|B)
# print(A&B)
# print(A-B)
# print(B-A)
# <<<<<<---------->>>>>>>>

# age=int(input("Enter your Age: "))
# if age>=18:
#     print("You are an Adult.")
# else:
#     print("You aer a Minor.")

# num=int(input("Enter the Number: "))

# if num>0:
#     print("Positive.")
# elif num==0:
#     print("Zero")
# else:
#     print("Negative.")

# username = "admin"
# password = "12345"

# username=input("Enter your username: ")
# password=int(input("Enter your password: "))

# if username=="admin" and password==12345:
#     print("Login successfull.")
# elif username=="admin":
#     print("Wrong password")
# else:
#     print("Wrong username")

# person = {
#     "first_name": "Abu",
#     "last_name": "Saif",
#     "age": 250,
#     "country": "Dhaka",
#     "is_married": False
# }

# if person["is_married"]==False and person["country"]=="Dhaka":
#     print("He is not married and lives in Dhaka.")
# else:
#     print("Wrong Person!")


# age=int(input("Enter your Age: "))

# if age<18:
#     print("You are a minor.")
# else:
#     country=input("Enter your Country: ").lower()
#     student=input("Are you a student? (y/n)").lower()
    
#     if age>=18 and student=="y":
#         print("You are an adult Student.")
#     elif age>=18 and student=="n" and country=="bangladesh":
#         print("Adult from Bangladesh.")
#     elif age>=18 and student=="n" and country=="dhaka":
#         print("Adult From Dhaka")
#     else:
#         print("Other.")

# age=int(input("Enter your Age: "))
# if age<5:
#     print("Free.")
# elif 5<=age<=26:
#     student=input("Student? (y/n)")
#     if student=="y":
#         print("Student ticket: $3")
#     else:
#         if 5<= age <=17:
#             print("Child ticket: $5")
#         elif 18<= age<=64:
#             print("Adult ticket: $10")
#         elif age>=65:
#             print("Senior ticket: $6")


# user_name = input("Username: ")
# password = input("Password: ")
# age = int(input("Age: "))

# if user_name == "admin":

#     if password == "python123":

#         if age >= 18:
#             print("Login successful.\nWelcome admin.")
#         else:
#             print("Admin account requires you to be 18+")

#     else:
#         print("Wrong password.")

# else:
#     print("Wrong username.")

# age=int(input("Age: "))
# student=input("Student? (y/n)")
# week=input("Day of the week: ").lower()

# if age<5:
#     print("Free ticket.")
# else:
#     if student=="y":
#         print("Student ticket: $7")
#     else:
            
#         if week=="tuesday":
#             if 5<=age<=17:
#                 print("Child ticket: $4")
#             elif 18<=age<=64:
#                 print("Adult ticket: $8")
#             elif age>=65:
#                     print("Senior ticket: $5")
#         else:
#             if 5<=age<=17:
#                 print("Child ticket: $5")
#             elif 18<=age<=64:
#                 print("Adult ticket: $10")
#             elif age>=65:
#                 print("Senior ticket: $6")


# correct_pin = "1234"
# balance = 1000

# pin=input("Enter your PIN: ")
# amount=int(input("Enter withdrawal amount: "))

# if pin!=correct_pin:
#     print("Incorrect PIN.")
# else:
#     if amount>balance:
#         print("Insufficient Balance.")
#     elif amount<=0:
#         print("Invalid amount.")
#     elif amount>=500:
#         print("Daily withdrawal limit is $500.")
#     else:
#         print(f"Withdrawal successful.\nRemaining balance: ${balance-amount}")

# amount=float(input("Enter bill amount: "))
# member=input("Are you a member? (y/n)").lower().strip()

# if member=="n":
#     print(f"Original bill: ${amount}")
#     print("Discount: $0")
#     print(f"Final bill: ${amount}")
# elif member=="y":
#     if amount<20:
#         print(f"Original bill: ${amount}")
#         print("Discount: $0")
#         print(f"Final bill: ${amount}")
#     elif 20<=amount<=49:
#         print(f"Original bill: ${amount}")
#         d_amount=amount*0.1
#         print(f"Discount: {d_amount}")
#         print(f"Final bill: ${amount-d_amount}")
#     elif 50<=amount<=99:
#         print(f"Original bill: ${amount}")
#         d_amount=amount*0.15
#         print(f"Discount: {d_amount}")
#         print(f"Final bill: ${amount-d_amount}")
#     elif amount>=100:
#         print(f"Original bill: ${amount}")
#         d_amount=amount*0.2
#         print(f"Discount: {d_amount}")
#         print(f"Final bill: ${amount-d_amount}")
# else:
#     print("Invalid!")


# price=float(input("Enter product price:: "))
# quantity=int(input("Enter quantity: "))
# member=input("Are you a premium member? (y/n)")
# total=price*quantity
# if price<=0 or quantity <=0:
#     print("Invalid!")
#     discount=None
# else:
#     if member=="n":
#         discount=0
#         free_shipping=10
#     elif member=="y":
#         if total>=100:
#             discount=total*0.2
#             free_shipping=0
#         else:
#             if 50<=total<=99.99:
#                 discount=total*0.1
#                 free_shipping=10
#             elif total<50:
#                 discount=0
#                 free_shipping=10
#     else:
#         discount=None

#     if discount is not None:
#         print(f"Subtotal:${total}\nDiscount:${discount}\nShippint:${free_shipping}\nFinal Total: ${(total+free_shipping)-discount}")

