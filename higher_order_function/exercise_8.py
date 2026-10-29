countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

new_country=filter(lambda country:len(country)>=6,countries)

print(list(new_country))