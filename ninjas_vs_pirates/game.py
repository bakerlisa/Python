import random
from classes.ninja import Ninja
from classes.pirate import Pirate


#Chose character
character = input('Ninja or Pirate?\n')

if(character.lower() == 'ninja'):
    print("RRRRRR Maty you chose wrong!")
    opponent = Pirate("Jack Sparrow")
    player = Ninja("Michelanglo")
    opponent.attack(player)
    print("There's no honor in theives, Your opponent has attacked! \n")
    print(f"Player health is at: {player.health}")
elif(character.lower() == 'pirate'):
    opponent = Ninja("Michelanglo")
    player = Pirate("Jack Sparrow")
    print("This will be your downfall pirate. You'll never see me coming\n")
    player.health
else:
    print("I didn't get that")
    character = input('Ninja or Pirate?\n')

# FIRST ACTION
opponents_turn = False

while(player.health > 0 and opponent.health > 0):
    if opponents_turn == True:
        # OPPONENT MOVES
        response = ["attack","attack","train","attack","rest","attack","block","attack","attack","attack","train","attack","train"]
        num = random.randint(0,len(response) - 1)
        
        if response[num] == "attack":
            print("\nopponent has decided to attack")
            print(f"Player Health at: {player.health}")
            opponent.attack(player,message=False)
        elif response[num] == "train":
            print("\nopponent has decided to train")
            opponent.train(message=False)
            player.health
        elif response[num] == "rest":
            print("\nopponent has decided to rest")
            opponent.rest(message=False)
            player.health
        elif response[num] == "block":
            print("\nopponent has earned a block")
            opponent.block == True
        opponents_turn = False
    else:
        # PLAYER MOVES
        choose_option = input("Your move: attack, train, rest, block\n").lower()
        if choose_option == "attack":
            player.attack(opponent)
            print(f"\n OPPONENT health {opponent.health}\n")
        elif choose_option == "train":
            days = input("\nHow many days would you like to train\n")
            player.train(int(days))
        elif choose_option == "rest":
            player.rest()
        elif choose_option == "block":
            print("block")
        else:
            choose_option = input("I didn't get that: attack, train, rest, block\n").lower()
        opponents_turn = True

if player.health < 0:
    print(f"\n\n Game over \n\n")
elif opponent.health < 0:
    print(f"\n\n You Won!!!\n\n")



# Try adding sub classes -Like next level type classed next also change the names to trex vs dragins - so much cooler!