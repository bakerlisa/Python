class BankAccount:
    totalBankUsers = 0

    def __init__(self,balance = 0,int_rate = .2):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.totalBankUsers += 1


    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(amount > 0):    
            self.balance -= amount
        else:
            print("Action denied. Insufficient funds")
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):    
            self.balance = self.balance / self.int_rate
            return self
    @classmethod
    def totalBankAccounts(cls):
        print(f"There are {cls.totalBankUsers} at this bank")


account1 = BankAccount(1000,.3)
account1.deposit(100).deposit(100).deposit(100).withdraw(500).yield_interest()
account1.display_account_info()

account2 = BankAccount(10000,.5)
account2.deposit(500).deposit(500).withdraw(1000).withdraw(2000).withdraw(3000).withdraw(30).yield_interest()

account2.display_account_info()

BankAccount.totalBankAccounts()
