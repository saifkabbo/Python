countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

new_country=filter(lambda country:country.startswith("E"),countries)

print(list(new_country))