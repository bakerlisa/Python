class Pirate:

    def __init__(self,name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.block = False
        self.battles = 0

    def show_stats(self):
        print(f"Your Stats - Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack (self,target,message=True):
        if self.block == True:
            self.block = False
        elif target.speed > 15:
            if message == True: 
                print("opponent avoided attack")
            target.speed -= 2
        else:
            target.health -= self.strength
        self.battles += 1
        return self    

    def rest (self, message=True):
        if self.battles == 3:
            self.health += 5
        elif self.battles == 5:
            self.health += 5
        elif self.battles == 10:
            self.health += 10
            self.speed += 10
        else:    
            if message == True:    
                print(f"{self.name} wasn't as tired as he thought. He went to a brothel and drank too much wine")
            self.health -= 2
        return self

    def block (self, message=True):   
        self.block == True 
        if self.battles > 3:    
            self.health += 3 
            if message == True:   
                print("battle greenie. You earned 3 health points")
        elif self.battles > 10:
            self.health += 5
            self.health += 3   
            if message == True:
                print("battle seasoned. You earned 5 health points and 3 speed points")
        elif self.battles > 20:
            self.health += 8   
            self.speed += 8
            if message == True:    
                print("battle seasoned. You earned 8 health points and 8 speed")
        return self

    def train (self,days = 0,message=True):
        if days > 5:
            self.speed += 2
        else:
            self.strength += 2
            self.speed += 2
        return self

