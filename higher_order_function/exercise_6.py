countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

new_country=filter(lambda country:"land" in country,countries)

print(list(new_country))