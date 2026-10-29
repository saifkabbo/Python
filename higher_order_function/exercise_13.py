countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

from functools import reduce

new_country=reduce(lambda a,b:a+", "+b,countries)

new_country=new_country.replace(", Iceland",", and Iceland")

print(new_country)