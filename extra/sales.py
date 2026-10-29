import csv

with open("sales.csv","r",encoding="utf-8") as f:
    text=csv.DictReader(f)
    total=0
    name=None
    for row in text:
       if int(row["price"])*int(row["quantity"])>total:
           total=int(row["price"])*int(row["quantity"])
           name=row["product"]
    print(f"Hightest value: {name}\nTotal value: {total}")
