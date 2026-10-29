class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        return f'Woof! My name is {self.name}'
    def get_age(self):
        return self.age


dog = Dog("Buddy", 3)

print(dog.bark())
print(dog.get_age()+5)