class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def display_user_balance(self):
        print(self.name, "has a user balance of:", self.account_balance)
        return self

    def make_withdrawl(self,amount):
        if(amount > 0):    
            self.account_balance -= amount
        else:
            print("Action denied. Insufficient funds")
        return self

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def transfer_money(self,amount,user):
        self.account_balance -= amount
        user.make_deposit(amount)
        return self

lisa = User("lisa","lisa@gmail.com")

lisa.make_deposit(200)
lisa.make_deposit(400)
lisa.make_deposit(1000)
lisa.make_withdrawl(600)
# lisa.display_user_balance()


elliot = User("elliot","elliot@elliot.com")
elliot.make_deposit(2000)
elliot.make_deposit(2000)
elliot.make_withdrawl(100)
elliot.make_withdrawl(400)

nat = User("Natalie","nat@nat.com")
nat.make_deposit(50)
nat.make_deposit(20)
nat.make_withdrawl(15)
nat.make_withdrawl(30)

#BONUS
# print(lisa.account_balance)
# print(nat.account_balance) 

lisa.transfer_money(100,nat)
lisa.display_user_balance()
nat.display_user_balance()