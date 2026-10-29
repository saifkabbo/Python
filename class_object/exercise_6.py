class Calculator():
    def __init__(self):
        pass
    def add(self,num_1,num_2):
        return  num_1+num_2
    def multiply(self,num_1,num_2):
        return num_1*num_2
    def show_result(self,value):
         print(f'Result: {value}')

calc = Calculator()

result = calc.add(10, 5)
calc.show_result(result)

result2 = calc.multiply(4, 3)
calc.show_result(result2)