class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def remove_item(self, name):
        self.items = [item for item in self.items if item[0] != name]

    def get_total(self):
        return sum(price for _, price in self.items)

    def show_items(self):
        print(self.items)

# cart.add_item("Book", 200)
# cart.add_item("Pen", 50)
# cart.add_item("Bag", 800)

# print(cart.get_total())  # 1050

# cart.remove_item("Pen")

# print(cart.get_total())  # 1000
# cart.remove_item("Laptop")
# cart.show_items()

cart = ShoppingCart()

cart.add_item("Book", 200)
cart.add_item("Pen", 50)
cart.add_item("Bag", 800)

cart.show_items()

cart.remove_item("Pen")

cart.get_total()
cart.show_items()