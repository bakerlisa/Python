from superhero import SuperHero

# RichTechies
class RichTech(SuperHero):
    def __init__(self, name, ability, suit, net_worth:int, company, health=100, attack_power=3):
        super().__init__(name,ability,suit,health,attack_power)
        self.net_worth = net_worth
        self.company = company

    # modify the intro - Override
    def intro(self):                                        
        super().intro()
        print(f"By the way I'm super rich, worth like a ${self.net_worth} but who cares")
        