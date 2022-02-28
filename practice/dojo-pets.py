class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        # self.pet = Pet(name = "",type = "pet",tricks = [],health = 25,engery = 50)
    
    def walk(self,target):
        target.play()
        return self

    def feed(self,target):
        target.eat()
        return self

    def bahte(self):
        target.noise()
        return self


class Pet:
    def __init__(self,name,type,tricks,health,engery):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health= health
        self.engery = engery

    def sleep(self):
        pass

    def eat(self):
        pass

    def play(self):
        pass

    def noise():
        pass

ninjaOne = Ninja("Lisa","Boradhead","Bones","Kibble")
ninjaOne.dog = Pet("Gus","Pomchi","['sit','stay','stand]",100,50)
ninjaOne.cat = Pet("Whikers","Tom","sleeping",100,0)

print(ninjaOne.dog.name)
print(ninjaOne.cat.name)


# 1. Do I have to pass in the pet "accisation class" when I set up my ninja?
#     # ninjaOne = Ninja("Lisa","Boradhead","pet","Bones","Kibble")
# 2. Is there a way to set up assciation and Ninja class at the same time?
#     # ninjaOne = Ninja("Lisa","Boradhead","Bones","Kibble",Pet("Gus","Pomchi","['sit','stay','stand]",100,50))