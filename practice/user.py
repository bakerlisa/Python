class User:
    bank_name = "First National Dojo"

    def __init__(self,name,email,account_balance = 0):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def display_user_balance(self,message = ""):
        print(self.account_balance)
        if message == "error":
            print(f"Insuffient funds: Account balance: {self.account_balance}")
        elif message == "deposit":
            print(f"Deposit Complete. Account balance: {self.account_balance}")
        elif message == "withdrawl":
            print(f"Transfer Complete. Account balance: {self.account_balance}")
        else:
            print(self.account_balance)

        return self

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        if(self.account_balance - amount <= -1):
            self.display_user_balance("error")
        else:    
            self.account_balance -= amount;
            self.display_user_balance("withdrawl")
        return self

    def transfer_money(self,other_user,amount):
        if self.account_balance - amount >= -1:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            self.display_user_balance("withdrawl")
            other_user.display_user_balance("deposit")
        else:
            print(f"{self.name} has insuffient funds for this transfer")
        return self


newAccount1 = User("Lisa Broadhead","lb@gmail.com",5000)
newAccount2 = User("Elliot Broadhead","eb@gmail.com",500)

newAccount2.make_withdrawal(300).make_withdrawal(200).make_deposit(400)

newAccount3 = User("Gus Broadhead","gus@gmail.com")
# newAccount3.make_deposit(300).make_deposit(300).make_deposit(400)
# print(f"Account: {newAccount1.name}: {newAccount1.email} has a blanace of {newAccount1.account_balance}")

# newAccount2.make_deposit(100)
# newAccount2.make_withdrawal(1000)
# print(newAccount1.display_user_balance)
# newAccount2.transfer_money(newAccount3,400)
# newAccount2.display_user_balance()
newAccount2.display_user_balance()

