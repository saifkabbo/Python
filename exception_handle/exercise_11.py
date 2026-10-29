def process_numbers(*args):
    try:
     return sum(args)/len(args)
    except ZeroDivisionError:
     return "No number provided."

# print(process_numbers(10, 20, 30))
print(process_numbers())