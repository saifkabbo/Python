import requests
from statistics import*
url='https://api.thecatapi.com/v1/breeds'
cat_api='live_rx3ViewCDvbgf5njF3G3AUR5R6TaEEvD8AsuhAVEoYbXEdCIcl1mFDNoQciNVwo8'
header={
    "x-api-key": cat_api
}
response=requests.get(url,headers=header)
data=response.json()

cat_weight=[]
for cat in data:
    cat_weight_metric=cat['weight']['metric'].split("-")
    cat_weight.append(cat_weight_metric)

# weight=data[0]["weight"]["metric"].split("-")
# average=(float(weight[0])+float(weight[1]))/2
# print(round(average,2))
cat_weight_1=[]
for i in range(len(cat_weight)):
    if len(cat_weight[i])==2:
        # cat_weight_1.append(float(cat_weight[i][0]))
        # cat_weight_1.append(float(cat_weight[i][1]))
        cat_weight_1.append(((float(cat_weight[i][0]))+(float(cat_weight[i][1])))/2)


minimum=min(cat_weight_1)
maximum=max(cat_weight_1)
mean_value=mean(cat_weight_1)
standart_deviation=stdev(cat_weight_1)
median_value=median(cat_weight_1)
print(f"Minimun weight: {minimum}kg\nMaximum weight: {maximum}kg\nMean weight: {mean_value}kg\nstandart deviation weight: {standart_deviation}kg\nMedian weight: {median_value}kg")

