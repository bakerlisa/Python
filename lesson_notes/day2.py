# OOP:
# Class
# Attributes - have (tool belt)
# Methods - what they can do
# Instance/Object - different instances (like ifferent types of dogs!)
# 
# Public - everyone or anyone can access
# Private - where childern can't inherit, but instances do
# Protected - instances and childern can inherit 

    #self is like the this in JS

# class User:
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def greeting(self):
#         print(f"Hello my name is {self.first_name}!")

# lisa = User("Lisa", "Baker", 90)
# lisa.greeting()

#  ******** CLASS LESSON NOTES:
    # class Array
        # when we call an array there's a built in method called length
# class Characters:
#     def __init__(self,name,age):
#         self.name = self
#         self.age = age
    
#     def intro(self):
#         print("Hi my name is {name}")

# class SuperHero:
#     def __init__(self,ability,costume,team,name,weakness):
#         self.ability = ability
#         self.costume = costume
#         self.team = team
#         self.costume = costume
#         self.weakness = weakness

#     def fight(self):
#         print("FIGHT")

#     def getDressed(self):
#         print("Tights and tight")

#     def activateAbility(self,abty):
#         # why does this concatination not work
#         print(f"activating {abty}")

#         # but these do
#         # print("activating {}".format(abty))
#         # print("activating " + abty)
#         # print("activating " , abty)

#     def joinTeam(self):
#         print("DC is ok but Marvel is better")


# mike = SuperHero(["flying","fire","shrink"],"tights","DC","MsMarvel","sleep")
# mike.activateAbility(mike.ability[1])
# # mike.activateAbility(len(mike.ability)) 
# # mike.getDressed()



#  ******** READING: LESSON NOTES:
# class Drinks:
#     people = 0
#     tables = 0

#     def __init__(self,customer,drink,size,cost,alcohol,caffeinated):
#         self.customer = customer
#         self.drink = drink
#         self.size = size
#         self.cost = cost
#         self.alcohol = alcohol
#         self.caffeinated = caffeinated
#         Drinks.people += len(customer)
#         Drinks.tables += 1
    
#     def greeting(self,customer,drink):
#         print(f"Hello {customer} just a {drink} for you today?")
    
#     @classmethod
#     def totalPeople(cls):
#         if(cls.people == 0):
#             print(f"No one here")
#         elif(cls.people == 1):
#             print(f"There's a bro in the house!")
#         else:
#             print(f"0s depressive, 1s a friends, but {cls.people}s a party! Raise the roof!! ")
    
#     @classmethod
#     def totalTables(cls):
#         print(f"waiter there are people at {cls.tables} table. Chop Chop")
    

# table1 = Drinks(["Karie","Mary","Harry","Barrie"],"water","sm","1.00",False,False)

# table1.greeting(table1.customer,table1.drink)

# Drinks.totalTables()

class SuperHero:
    totalSuperHeros = 0

    def __init__(self,name,ability,suit,weakness,health = 100, attack_power = 25):
        self.name = name
        self.ability = ability
        self.suit = suit
        self.health = health
        self.weakness = weakness
        self.attack_power = attack_power
        SuperHero.totalSuperHeros += 1
    
    def intro(self):
        print(f"Weeeeeeeeel-come super hero {self.name}.You'll know him by the {self.suit} he wears and his amazing ability of {self.ability}. But never give him {self.weakness}")
        return self

    def attack(self,target):
        if(target.health < self.attack_power):
            print(f"{target.name} is Dead. You can't attack Ghosts")
        else:    
            target.health -= self.attack_power
            print(f"{self.name} just attacked {target.name} with {self.ability}. {target.name} lost {self.attack_power} health. Health at {target.health}")
        return self
    
    def train(self,numOfDays):
        self.attack_power += (5 * numOfDays)
        print(f"{self.name} went to the Dojo to train for {numOfDays} days. His attack power is now at {self.attack_power}")
        if(numOfDays >= 7):
            self.health += (numOfDays * 2)
            print(f"He trained for over a week, his health has increased to {numOfDays * 2} points")
        return self

    @classmethod
    def totalPopulation(cls):
        print(f"Total Super Hero population is {cls.totalSuperHeros}")

super_hero1 = SuperHero("Jim","Making Slim Jims","Overalls","shirts",500)
super_hero2 = SuperHero("Rafaelangelo", "The Power of 2 Turtles", "Just a headband","turtles")
super_hero3 = SuperHero("Felix","CSS Reducing Skills","gold plated armour","HTML")

super_hero1.intro()
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.train(10).attack(super_hero2)
super_hero2.train(10)

SuperHero.totalPopulation()