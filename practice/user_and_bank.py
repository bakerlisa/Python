class Accounts:
    bank_name = "Dojo National Bank"
    total_bank_accounts = 0

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        Accounts.total_bank_accounts += 1

    def deposit(self,amount):
        self.balance += amount
        self.display_account_info("deposit")
        return self

    def withdrawl(self,amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            self.display_account_info("withdrawl")
        else:
            self.display_account_info("error")
        return self

    def yield_interst(self):
        self.balance += self.int_rate * self.balance
        return self

    def display_account_info(self,message=""):
        if message == "error":
            self.balance
        elif message == "deposit":
            print(f"Deposit Complete. Account balance: {self.balance}")
        elif message == "withdrawl":
            print(f"Transfer Complete. Account balance: {self.balance}")
        else:
            print(self.balance)
        return self

    @classmethod
    def total_bankers(cls):
        print(f"The totoal number of bankers at {cls.bank_name} is {cls.total_bank_accounts}")

class User:
    def __init__(self,name,email,checking = 0,savings = 0):
        self.name = name
        self.email = email
        self.checking = Accounts(.5,checking)
        self.savings = Accounts(.25,savings)

    def display_user_balance(self,target,message = ""):
        target.display_account_info()
        return self

    def make_deposit(self,target,amount):
        target.deposit(amount)
        return self

    def make_withdrawal(self,target,amount):
        target.withdrawl(amount)
        return self

    def transfer_money(self,target,other_account,amount):
        if target.balance - amount >= -1:
            target.withdrawl(amount)
            other_account.deposit(amount)
        else:
            print(f"You have insuffient funds for this transfer")
        return self

newAccount1 = User("Lisa Broadhead","lb@gmail.com",1000,100)
# newAccount1.make_deposit(newAccount1.checking,300)
# newAccount1.make_withdrawal(newAccount1.checking,500)
# newAccount1.transfer_money(newAccount1.checking,newAccount1.savings,500)

newAccount2 = User("Elliot Broadhead","eb@gmail.com",500,50)
newAccount3 = User("Gus Broadhead","gus@gmail.com",0,0)

newAccount1.transfer_money(newAccount1.checking,newAccount2.savings,500)
# newAccount2.make_deposit(100)
# Accounts.total_bankers()
