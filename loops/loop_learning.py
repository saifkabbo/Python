# Count=0
# while Count<5:
#     print(Count)
#     Count+=1
# else:
#     print(f"Total:{Count}") 

# while Count<5:
#     if Count==3:
#         Count+=1
#         continue
#     print(Count)
#     Count=Count+1

# count=0
# while count<5:
#     if count==3:
#         count+=1
#         continue
#     print(count)
#     count+=1

# num=[0,1,2,3,4]
# for number in num:
#     print(number)
# language="Python"
# # for letter in language:
# #     print(letter)

# for i in range(len(language)):
#     print(language[i])

# number=(1,2,3,4)
# for num in number:
#     print(num)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# print(person)
# for key in person:
#     print(key)
# for value in person.items():
#     print(value)

# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# # print(it_companies)
# for company in it_companies:
#     print(company)

# # person["first_name"].remove()
# person["last_name"]="Saif"
# person["middle_name"]="Kabbo"
# print(person)

# print(person.get("num","not found"))

# num=(1,2,3,4,5,6)
# for number in num:
    
#     if number==3:
#         continue
#     print(number)

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# for number in range(1,11):
#     print(number)

# lst=list(range(1,11))
# st=set(range(1,11))
# tp=tuple(range(1,11))
# print(lst)
# print(st)
# print(tp)

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11
# else:
#     print('The loop stops at', number)

# for number in range(6):
#     pass
# print(number)