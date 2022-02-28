class BankAccount:
    totalBankAccounts = 0

    def __init__(self,balance = 0,int_rate = .2):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.totalBankAccounts += 1

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
    def totalAccounts(cls):
        print(f"There are {cls.totalBankAccounts} at this bank")

class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .02, balance = 0)
        self.savings = BankAccount(int_rate = .01, balance = 500)
    
    def make_withdrawl(self,amount,target):
        target.withdraw(amount)
        return self

    def make_deposit(self,amount,target):
        target.deposit(amount)
        return self
    
    def display_user_balance(self,target):
        target.display_account_info()
        return self

    def transfer_money(self,amount,target,transferer):
        target(amount)
        transferer.make_deposit(amount)
        return self

account1 = User("lisa","lisa@gmail.com")

# print(lisa.account_balance)
# lisa.display_user_balance(50)

# account1.make_withdrawl(100,"savings")

#account1.savings.withdraw(50)
#account1.savings.display_account_info()


# BONUS!!
account1.display_user_balance(account1.savings)
account1.make_withdrawl(50,account1.savings)
account1.display_user_balance(account1.savings)