# # # # # # def sum_numbers(nums):  # normal function
# # # # # #     return sum(nums)    # a sad function abusing the built-in sum function :<

# # # # # # def higher_order_function(f, lst):  # function as a parameter
# # # # # #     summation = f(lst)
# # # # # #     return summation
# # # # # # result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# # # # # # print(result)       # 15

# # # # # return value

# # # # def square(x):          # a square function
# # # #     return x ** 2

# # # # def cube(x):            # a cube function
# # # #     return x ** 3

# # # # def absolute(x):        # an absolute value function
# # # #     if x >= 0:
# # # #         return x
# # # #     else:
# # # #         return -(x)

# # # # def higher_order_function(type): # a higher order function returning a function
# # # #     if type == 'square':
# # # #         return square
# # # #     elif type == 'cube':
# # # #         return cube
# # # #     elif type == 'absolute':
# # # #         return absolute

# # # # result = higher_order_function('square')
# # # # print(result(3))       # 9
# # # # result = higher_order_function('cube')
# # # # print(result(3))       # 27
# # # # result = higher_order_function('absolute')
# # # # print(result(-3))      # 3

# # # # #Python Closures

# # # def add_ten():
# # #     ten = 10
# # #     def add(num):
# # #         return num + ten
# # #     return add

# # # closure_result = add_ten()
# # # print(closure_result(5))  # 15
# # # print(closure_result(10))  # 20

# # # Python Decorators

# # # Normal function
# # def greeting():
# #     return 'Welcome to Python'
# # def uppercase_decorator(function):
# #     def wrapper():
# #         func = function()
# #         make_uppercase = func.upper()
# #         return make_uppercase
# #     return wrapper
# # g = uppercase_decorator(greeting)
# # print(g())          # WELCOME TO PYTHON

# # ## Let us implement the example above with a decorator

# # '''This decorator function is a higher order function
# # that takes a function as a parameter'''
# # def uppercase_decorator(function):
# #     def wrapper():
# #         func = function()
# #         make_uppercase = func.upper()
# #         return make_uppercase
# #     return wrapper
# # @uppercase_decorator
# # def greeting():
# #     return 'Welcome to Python'
# # print(greeting())   # WELCOME TO PYTHON

# def uppercase_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
# def split_string(func):
#     def wrapper():
#        return func().split()
#     return wrapper
# @split_string
# @uppercase_decorator
# def greeting():
#     return "Welcome Saif!"
# # g=uppercase_decorator(greeting)
# # print(uppercase_decorator(greeting)())
# print(greeting())

# def decorator_with_parameters(func):
#     def wrapper(**kwargs):
#         return func(**kwargs).upper()
#     return wrapper

# @decorator_with_parameters
# def introduction(name,country):
#     return f"I'm {name} and i'm from {country}"

# print(introduction(name="Saif",country="Bangladesh"))

# map()

# names = ['Abu', 'Saif', 'Kabbo', 'Abraham']

# upper_names=map(lambda name:name.upper(),names)

# print(list(upper_names))

# filter()

# numbers = [1, 2, 3, 4, 5]  # iterable

# def is_odd(num):
#     if num % 2 != 0:
#         return True
#     return False

# odd_numbers = filter(is_odd, numbers)
# print(list(odd_numbers))       # [1, 3, 5]

# reduce()
# from functools import reduce


