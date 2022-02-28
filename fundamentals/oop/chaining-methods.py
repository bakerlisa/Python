


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # def display_user_balance(self):
    #     print(self.account_balance)

    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def transfer_money(self,amount,user):
        self.account_balance -= amount
        user.make_deposit(amount)
        return self

lisa = User("lisa","lisa@gmail.com")

lisa.make_deposit(200).make_deposit(400).make_deposit(1000).make_withdrawl(600)

elliot = User("elliot","elliot@elliot.com")
elliot.make_deposit(2000).make_deposit(2000).make_withdrawl(100).make_withdrawl(400)

nat = User("Natalie","nat@nat.com")
nat.make_deposit(50).make_deposit(20).make_withdrawl(15).make_withdrawl(30)

#BONUS
# print(lisa.account_balance)
# print(nat.account_balance) 

lisa.transfer_money(100,nat)

# print(lisa.account_balance)
# print(nat.account_balance)