from pets import Pet

class Ninja():
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


# pet1 = Ninja("lisa","broadhead","dog","bones","kibble","Gus","dog","sit")
pet1 = Ninja("lisa","broadhead","dog","bones","kibble")

pet1.walk(pet1.pet).feed(pet1.pet,"kibble").bathe(pet1.pet)
pet1.walk(pet1.pet2)
pet1.bathe(pet1.pet3)


# print(pet.pet_food)
# pet.walk(pet.name)