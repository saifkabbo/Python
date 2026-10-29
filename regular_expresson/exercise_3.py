import re

def is_valid_variable(x):
 print(bool(re.match(r"^[A-Za-z_][A-Za-z0-9_]*$",x)))


is_valid_variable('1first_name')


    