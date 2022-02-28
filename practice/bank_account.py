class Accounts:
    bank_name = "Dojo National Bank"
    total_bank_accounts = 0

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        Accounts.total_bank_accounts += 1

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdrawl(self,amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Has an account balance of: {self.balance}")
        return self

    def yield_interst(self):
        self.balance += self.int_rate * self.balance
        return self

    @classmethod
    def total_bankers(cls):
        print(f"The totoal number of bankers at {cls.bank_name} is {cls.total_bank_accounts}")

account1 = Accounts(.03,5000)
account1.withdrawl(5000)
account1.display_account_info()

account2 = Accounts(.05,10000)
Accounts.total_bankers()