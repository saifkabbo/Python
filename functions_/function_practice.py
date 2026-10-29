# def add_two_numbers(num1,num2):
#     total=num1+num2
#     return total
# print(add_two_numbers(2,3))

# def area_of_circle(r):
#     area=3.14*r*r
#     return area
# print(area_of_circle(10))

# def add_all_nums(*args):
#     total=0
#     for item in args:
#         if isinstance(item,int):
#             total+=item
#         else:
#             print(f"{item} is not a number.")
#     return total

# print(add_all_nums(2, 4, 6, 8))

# def convert_celsius_to_fahrenheit(c):
#     f=(c*9/5)+32
#     return f
# print(convert_celsius_to_fahrenheit(32))

# def check_season(*args):

#     for month in args:
#         if isinstance(month,str):

#             if month in ["december", "january", "february"]:
#                 print("Winter")

#             elif month in ["march", "april", "may"]:
#                 print("Spring")

#             elif month in ["june", "july", "august"]:
#                 print("Summer")

#             elif month in ["september", "october", "november"]:
#                 print("Autumn")
#             else:
#                 print(f"{month} is not a month")
#         else:
#             print(f"{month} is not a month.")


# check_season("march", "july", "november","hello")

# def calculate_slope(x1,y1,x2,y2):
#     x=x2-x1
#     y=y2-y1
#     slope=y/x
#     # print(slope)
#     return slope
# print(calculate_slope(2,3,4,7))
# from math import sqrt
# def solve_quadratic_eqn(a,b,c):
#     s=b**2-4*a*c
#     if s<0:
#         x1=(f"{-b}+i{sqrt(abs(s))}")
#         x2=(f"{-b}-i{sqrt(abs(s))}")
#         return x1,x2
#     elif s>0:
#         x1=(-b+sqrt(abs(s)))/2*a
#         x2=(-b-sqrt(abs(s)))/2*a
#         return x1,x2
#     elif s==0:
#         x1=-b/2*a
#         x2=x1
#         return x1,x2
#     else:
#         return "Invalid!"

# print(solve_quadratic_eqn(1,2,3))

# def print_list(l):
#     for i in l:
#         print(i)

# print_list([1,2])

# lst=[1,2,3]

# def reverse_list(lst):
#     l=lst[::-1]
#     for i in l:
#         print(i)
# reverse_list(["C", "B", "A"])

# def capitalize_list_items(lst):
#     capitalize=list()
#     for i in lst:
#         i=i.capitalize()
#         capitalize.append(i)
#     print(capitalize)
# capitalize_list_items(["abu","saif","kabbo"])

# def add_item(lst, item):
#     lst.append(item)
#     return lst

# print(add_item(["md", "abu"], "saif"))

# def remove_item(lst,item):
#     if item in lst:
#         lst.remove(item)
#         print(lst)
#     else:
#         print(f"{item} not in the list")

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# # numbers = [2, 3, 7, 9]
# remove_item(food_stuff,'Orange')

# def sum_of_numbers(x):
#     total=0
#     for i in range(x+1):
#             total+=i
#     print(total)



        
# sum_of_numbers(100)

# def sum_of_odds(x):
#     even=0
#     odd=0
#     for i in range(x+1):
#         if i%2!=0:
#             odd+=i
#         else:
#             even+=i
#     print(f"Even total: {even}\nOdd total: {odd}")
# sum_of_odds(5)


# def evens_and_odds(x):
#     even_count=0
#     odd_count=0
#     for i in range(x+1):
#         if i%2==0:
#             even_count+=1
#         else:
#             odd_count+=1
#     print(f"The number of odds are: {odd_count}")
#     print(f"The number of evens are: {even_count}")

# evens_and_odds(100)

# def factorial(x):
#     if x==0:
#         print("1")
#     else:
#         fact=1
#         for i in range(1,x+1):
#             fact*=i
#         print(fact)
            
# factorial(3)

# def is_empty(x):
#     if len(x)==0:
#         print("False")
#     else:
#         print("True")
# is_empty(["Saif"])

# def calculate_mean(x):
#     total=sum(x)/len(x)
#     print(total)
# calculate_mean([1,2,3,4,5])

# median=lst[round((len(lst)/2))]
# print(median)

# def middle_value(l):
#     l.sort()
#     if len(l)%2!=0:
#         median=l[len(l)//2]
#     else:
#         a=l[len(l)//2-1]
#         b=l[len(l)//2]
#         median=(a+b)/2
#     print(median)

# middle_value([3,2,1,4])

# def calculate_mode(x):
#     counts={}
#     for i in x:
#         if i in counts:
#             counts[i]+=1
#         else:
#             counts[i]=1
#     largest=0
#     mode=None
#     for key,value in counts.items():
#         if value>largest:
#             largest=value
#             mode=key
#     print(mode)


# calculate_mode([1, 2, 2, 3, 3, 3, 3, 4])

# def calculate_range(x):
#     a=max(x)
#     b=min(x)
#     range_value=a-b
#     print(range_value)
# calculate_range([2, 5, 8, 10])

# def calculate_varience(x):
#     mean = sum(x)/len(x)
#     total=0
#     for i in x:
#         total+=(mean-i)**2
#     variance=total/len(x)
#     print(f"{variance:.6f}")

# calculate_varience([1, 2, 3])
# from math import sqrt
# def calculate_standart_daviation(x):

#     mean = sum(x)/len(x)
#     total=0
#     for i in x:
#         total+=(mean-i)**2
#     variance=total/len(x)
#     std=sqrt(variance)
#     print(f"Standart Daviation: {std}")

# calculate_standart_daviation([1, 2, 3])

# def greet(name="Guest"):
#     print(f"Hello {name}!")

# greet()

# def show_args(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)


# show_args(name="Saif", age=25, country="Bangladesh")

# def is_prime(x):
#     if x<2:
#     #  print(f"{x} is not prime.")
#      return False
#     if x==2:
#     #    print(f"{x} is prime")
#        return True
#     for i in range(2,x):
#        if x%i==0:
#         #   print(f"{x} is not prime
#           return False
#     else:
#     #  print(f"{x} is prime.")
#      return True
# print(is_prime())

# def main(y):
#    count=0
#    for i in range(y):
#       if is_prime(i):
#        count+=1
#    print(f"total prime number:{count}")

# main(100)

# def all_item(x):
#     for i in x:
#         if x.count(i)>1:
#           print("False.")
#           return
#     else:
#      print("True.")
#      return
# all_item([1,2,3])

# def all_item_same_type(x):
#     first_type=type(x[0])
#     for i in x:
#      if first_type!=type(i):
#       print("False.")
#       return
    
#     else:
#         print("True.")
#         return  

# all_item_same_type([1,2,3,"saif"])

# import keyword

# def valid_variable(x):
#     if not x.isidentifier() or keyword.iskeyword(x):
#         print("False.")
        
#     else:
#         print("True.")
        

# valid_variable("if")

# # # def count_item(numbers,target):
# # #     count=0
# # #     if target in numbers:
        
# # #         for i in numbers:
# # #             if target==i:
# # #                count+=1
# # #         print(f"{target} appear in {count} times.")
# # #     else:
# # #      print("The number not in the list.")

# # # count_item([1, 2, 2, 3, 2, 1,4],1)

# # def is_prime(x):
# #     if x<2:
# #         return False
# #     if x==2:
# #         return True
# #     for i in range(2,x):
# #         if x%i==0:
# #             return False
# #     else:
# #         return True

# # # print(is_prime(5))

# # def sum_prime(n):
# #     total=0
# #     for i in range(n):
# #         # print(i)
# #         if is_prime(i):
# #             total+=i
# #     print(f"Sum: {total}")

# # sum_prime(20)

# n=[10, 5, 8, 20, 15,20,20]
# from math import sqrt
# def second_large(x):
#     large=float("-inf")
#     s_large=float("-inf")
#     for i in x:
#         if i>large:
#          s_large=large
#          large=i
#         elif i>s_large and i!=large:
#           s_large=i
           
#     return s_large
        
# print(second_large([-10, -5, -20, -3]))


# def add_num(x=2,y=3):
#     total=x+y
#     print(total)
# add_num(6,4)


