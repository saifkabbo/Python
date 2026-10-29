countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

result = [[country.upper(), country[:3].upper(), capital.upper()]
          for item in countries
          for country, capital in item]

print(result)