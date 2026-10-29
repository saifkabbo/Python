import random

def unique():
 numbers=[]
 while len(numbers)<7:
  num=random.randint(0,9)
  if num not in numbers:
   numbers.append(num)
 return numbers
print(unique())


