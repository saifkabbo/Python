# # def generate_full_name ():
# #     first_name = 'Abu'
# #     last_name = 'Saif'
# #     space = ' '
# #     full_name = first_name + space + last_name
# #     print(full_name)
# # generate_full_name ()

# # def add_two_numbers ():
# #     num_one = 2
# #     num_two = 3
# #     total = num_one + num_two
# #     print(total)
# # add_two_numbers()

# # def generate_full_name ():
# #     first_name = 'Abu'
# #     last_name = 'Saif'
# #     space = ' '
# #     full_name = first_name + space + last_name
# #     return full_name
# # print(generate_full_name())

# # def add_two_numbers ():
# #     num_one = 2
# #     num_two = 3
# #     total = num_one + num_two
# #     return total
# # print(add_two_numbers())

# def greetings (name):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings("Saif"))

# def add_ten(num):
#     ten = 10
#     return num + ten
# print(add_ten(90))

# def square_number(x):
#     return x * x
# print(square_number(2))

# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(10))

# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     return total
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100))

# def generate_full_name(first_name,last_name):
#     full_name=first_name+" "+last_name
#     return full_name
# print(generate_full_name("Abu","Saif"))

# def sum_two_numbers (num_one, num_two):
#     sum = num_one + num_two
#     return sum
# print('Sum of two numbers: ', sum_two_numbers(1, 9))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age 

# print('Age: ', calculate_age(2021, 1819))

# def weight_of_object (mass, gravity):
#     weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# def find_even_numbers(n):
#     evens = []
#     for i in range(n + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(find_even_numbers(3))

# def greetings (name = 'kabbo'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())
# print(greetings('Saif'))

# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i) 
# generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

# def greet(name, location):
#     # Print a greeting message using the provided arguments
#     print("Hi there", name, "how is the weather in", location)

# greet("Saif","Dhaka")

# def arbitrary_named_args(**args):
#     # print("I received an arbitrary number of arguments, totaling", len(args))

#     # print("They are provided as a dictionary in my function:", type(args))

#     # print("Let's print them:")

#     for k, v in args.items():
#         print("* key:", k, "value:", v)

# arbitrary_named_args(name="name",age=22)

# def test(**kwargs):
#     print(kwargs)
# test(name="Saif",age=22)

