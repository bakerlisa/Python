class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Gus","dog","sit")
        self.pet2 = Pet("Zula","cat","sleeps")
        self.pet3 = Pet("Henery","goldfish","swims")
        self.pet4 = Pet("Garret","parrot","sings")
    
    def walk(self,pet):
        pet.play()
        return self
    
    def feed(self,pet,pet_food):
        pet.eat(pet_food)
        return self

    def bathe(self,pet):
        pet.noise()
        return self


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
        print(f"health is now at {self.health}")
        return self
    
    def noise(self):
        print("** bark bark ** You'll never take me alive ** bark bark **")
        return self
    
# pet1 = Ninja("lisa","broadhead","dog","bones","kibble","Gus","dog","sit")
pet1 = Ninja("lisa","broadhead","dog","bones","kibble")

pet1.walk(pet1.pet).feed(pet1.pet,"kibble").bathe(pet1.pet)


# print(pet.pet_food)
# pet.walk(pet.name)