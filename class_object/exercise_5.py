class PersonAccount():
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.incomes=[]
        self.expenses=[]
    def total_income(self):
        total_in=0
        for income in self.incomes:
            total_in+=income[0]
        return total_in
    def total_expense(self):
        total_ex=0
        for expense in self.expenses:
            total_ex+=expense[0]
        return total_ex
    def account_info(self):
        return f'Name: {self.firstname} {self.lastname}\nTotal Income: {self.total_income()}\nTotal Expenses: {self.total_expense()}\nRemaining Balance: {self.total_income() - self.total_expense()}'
    def add_income(self,amount,description):
        if amount>0:
            self.incomes.append((amount,description))
        else:
            print("Amount must be greater than zero.")
    def add_expense(self,amount,description):
        if amount>0:
            self.expenses.append((amount,description))
        else:
            print("amount,description use this formate.")
    def account_balance(self):
        return f'Remaining Balance: {self.total_income() - self.total_expense()}'
        
person_1=PersonAccount("Abu","Saif")
person_1.add_income(1000,"salaries")
person_1.add_expense(700,"rent")
person_1.add_income(500,"others")
person_1.add_expense(200,"food")
print(person_1.account_info())