class BankAccount():
    def __init__(self,owner,balance=0,):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited: {amount}")

    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw: {amount}")
    def show_balance(self):
         print(f'{self.owner} current balance is: ${self.balance}')
    def transfer(self, other_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred: ${amount}")
        else:
            print("Invalid amount or insufficient balance.")


account_1=BankAccount("Saif",1000)
account_2 = BankAccount("Kabbow", 500)
account_1.transfer(account_2, 200)

# person_1.show_balance()
# person_1.deposit(500)
# person_1.withdraw(200)
# person_1.show_balance()