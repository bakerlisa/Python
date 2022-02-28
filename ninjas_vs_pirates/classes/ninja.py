class Ninja:
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.block = False
        self.battles = 0
    
    def show_stats(self):
        print(f"Your Stats - Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self,target,message=True):
        if self.block == True:
            print("You've been blocked!")
            self.block = False
        else:
            if self.speed > 10:
                target.health -= self.strength + 10
            else:    
                target.health -= self.strength
        self.block = False
        return self
    
    def rest (self,message=True):
        if self.battles == 3:
            self.health += 5
        elif self.battles == 5:
            self.health += 5
        elif self.battles == 10:
            self.health += 10
            self.speed += 10
        else:    
            if message == True:    
                print(f"{self.name} wasn't tired, since he was able to save a town you earned a free block!")
            self.health -= 2
            self.block = True
        return self

    def block (self,message=True):
        if self.battles > 3:    
            self.block == True
            self.health += 3 
            if message == True:    
                print("battle mage. You earned 3 health points")
        elif self.battles > 10:
            self.block == True 
            self.health += 10   
            if message == True:    
                print("battle seasoned. You earned 10 health points")
        elif self.battles > 20:
            self.block == True 
            self.health += 10   
            self.speed += 5
            if message == True:    
                print("battle seasoned. You earned 15 health points and 5 speed")
        return self

    def train (self,days = 0,message=True):
        if days > 5:
            self.speed += 3
            if message == True:    
                print("Excellent training my student. you've eraned 3 speed points")
        else:
            self.strength += 4
            self.speed += 2
            if message == True:
                print("Because of your longer stay you've no eared 4 strength and 2 more speed points!")
        return self