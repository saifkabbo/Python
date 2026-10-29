with open("products.csv","r",encoding="utf-8") as f:
    highest_value=float("-inf")
    highest_value_product=None
    next(f)
    for row in f:
     name,price,quantity=row.split(",")
     if int(price)*int(quantity)>highest_value:
      highest_value=int(price)*int(quantity)
      highest_value_product=name
    print(f"{highest_value_product} = {highest_value}")