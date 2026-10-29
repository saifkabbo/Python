countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_countries=[{"country":country.upper(),"city":city.upper()} for row in countries for country,city in row]

print(new_countries)