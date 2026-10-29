import requests
from statistics import*
url='https://api.thecatapi.com/v1/breeds'
cat_api='live_rx3ViewCDvbgf5njF3G3AUR5R6TaEEvD8AsuhAVEoYbXEdCIcl1mFDNoQciNVwo8'
header={
    "x-api-key": cat_api
}
response=requests.get(url,headers=header)
data=response.json()
# print(data[0]['life_span'].split("-"))

cat_life_span=[]
for cat in data:
    cat_life_span.append(cat['life_span'].split("-"))

cat_life_span_1=[]
for i in range(len(cat_life_span)):
    if len(cat_life_span[i])==2:
        cat_life_span_1.append((float(cat_life_span[i][0])+float(cat_life_span[i][1]))/2)

maximum=max(cat_life_span_1)
minimum=min(cat_life_span_1)
mean_value=mean(cat_life_span_1)
standart_deviation=stdev(cat_life_span_1)
median_value=median(cat_life_span_1)
print(f"Minimun: {minimum}yr\nMaximum: {maximum}yr\nMean: {mean_value}yr\nstandart deviatio: {standart_deviation}yr\nMedian: {median_value}yr")