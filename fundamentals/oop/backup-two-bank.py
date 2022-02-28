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
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):    
            self.balance *= self.balance * self.int_rate
            return self
    @classmethod
    def totalBankAccounts(cls):
        print(f"There are {cls.totalBankUsers} at this bank")



class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate =.02, balance = 0)
    
    
lisa = User("lisa","lisa@gmail.com")
