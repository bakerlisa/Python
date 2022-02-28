class BankAccount:
    totalBankAccounts = 0

    def __init__(balance, int_rate):
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

    # def display_account_name(self):
    #     print(f"Account: {self.account_name}")

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

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
       
        # self.account.withdraw(amount)
        return self

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self,amount,transferee):
        self.account(amount)
        transferee.make_deposit(amount)
        return self

account1 = User("lisa","lisa@gmail.com")

# print(lisa.account_balance)
# lisa.display_user_balance(50)
# account1.make_withdrawl(500)

# account1.display_user_balance("savings")