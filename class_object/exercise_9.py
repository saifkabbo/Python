class Product():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def sell(self,amount):
        if amount>0:
            if amount<=self.quantity:
             self.quantity-=amount
             return f'Sale successfull!'
            else:
             return f'Not enough stock!'
        else:
            return f'Invalid amount!'
    def restock(self,amount):
        if amount>0:
         self.quantity+=amount
        else:
            return f'Invalid amount!'
    def get_total_value(self):
       return self.price*self.quantity

product = Product("Notebook", 50, 10)

# print(product.sell(3))
# print(product.quantity)
# print(product.get_total_value())
# product = Product("Notebook", 50, 7)
# print(product.sell(9))
# print(product.quantity)
# product = Product("Notebook", 50, 7)

# print(product.sell(-2))
# print(product.quantity)    
# product = Product("Notebook", 50, 10)

# product.restock(5)

# print(product.quantity)
# print(product.get_total_value())
product = Product("Notebook", 50, 10)

print(product.restock(-4))
print(product.quantity)