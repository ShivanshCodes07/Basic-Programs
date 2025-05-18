class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc
    #method to credit money
    def credit(self, amount):
        self.balance += amount
        print(amount, "credited to your account number : ", self.account_no)
        print("your current balance is :", self.balance)
    #method to debit money
    def debit(self, amount):
        self.balance -= amount
        print(amount, "debited from your account number : ", self.account_no)
        print("your current balance is :", self.balance)
    #method to check balance
    def check_balance(self):
        print("your current balance is :", self.balance)

acc1 = Account(1000 , 230134567896)
acc1.credit(2000)
acc1.debit(600)


    