from tkinter.font import names


class Dog:
    def __init__(self,name,breed, weight, age,color):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.age = age
        self.color = color

    def greeting(self):
        print(f"Hello {self.name} you're looking happy today!")
    
pet1 = Dog("Gus","Pomchi",17,1.5,"carmel")

pet1.greeting()

    