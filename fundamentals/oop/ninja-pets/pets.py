class Pet():
    def __init__(self,name,type,tricks,health = 100,engery = 25):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.engery = engery
    
    def sleep(self,):
        self.engery += 25
        return self

    def eat(self,pet_food):
        self.engery += 5
        self.health += 10
        print(f"I love {pet_food}!!")
        return self
    
    def play(self):
        self.health += 5
        if(self.type == "cat"):
            print("I'm a cat. I don not play unless I felli like it. I certainly d not go on walks **sniff**")  
        else:  
            print(f"health is now at {self.health}")
        return self
    
    def noise(self):
        print(self.type)
        if(self.type == "goldfish"):
            print("Since I'm a scholarly fish, how does one \"bathe\" a goldfish??")
        else:    
            print("** bark bark ** You'll never take me alive ** bark bark **")
        return self