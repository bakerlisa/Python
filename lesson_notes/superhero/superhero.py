from richtech import RichTech



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

# Mutants
class Mutant(SuperHero):
    def __init__(self, name, ability, suit, health = 100, attack_power = 3):
        super().__init__(name,ability,suit,health,attack_power)
        

# PeoleFromOtherPlanets
class PeoleFromOtherPlanets(SuperHero):
    def __init__(self,name,ability,suit,planet,health=100,attack_power=3):
        super().__init__(name,ability,suit,health,attack_power)



super_hero1 = SuperHero("Jim","Making Slim Jims","Overalls","shirts",500)
super_hero2 = SuperHero("Rafaelangelo", "The Power of 2 Turtles", "Just a headband","turtles")
super_hero3 = SuperHero("Felix","CSS Reducing Skills","gold plated armour","HTML")

super_hero1.intro()
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.train(10).attack(super_hero2)
super_hero2.train(10)

SuperHero.totalPopulation()

rich_tech1 = RichTech("IronMan","Genius Level Intellect", "Mach 5", 50000000)
rich_tech1.intro()