import requests
from statistics import*
url='https://api.thecatapi.com/v1/breeds'
cat_api='live_rx3ViewCDvbgf5njF3G3AUR5R6TaEEvD8AsuhAVEoYbXEdCIcl1mFDNoQciNVwo8'
header={
    "x-api-key": cat_api
}
response=requests.get(url,headers=header)
data=response.json()

# print(data[0]["origin"])
# print(data[0]['breed_group'])

cat_country_breed = {}

for cat in data:
    country = cat['origin']
    breed = cat['name']

    if country in cat_country_breed:
        cat_country_breed[country].append(breed)
    else:
        cat_country_breed[country] = [breed]

# print(cat_country_breed)

# country_frequency={}

# for cat in cat_country_breed:
#     country_frequency[cat]=len(cat_country_breed[cat])

# country_frequency=sorted(country_frequency.items(),key=lambda x:x[1],reverse=True)
# print(country_frequency)
