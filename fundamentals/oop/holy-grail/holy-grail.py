from calendar import c
import random

answers = []

def bridge_keeper():
    questions = ["what is your name","what is the airsepeed velocity of an unladen swallow?","what is the capital of Assyria"]
    correct_answer = "African of European"

    print("STOP!!!!!! \n Those who approach the bridge  of Death must answer these questions three, ere the other side they see \n")
    
    name = input("What is your name? ")
    quest = input("what is your quest? ")
    random_question = random.randint(0,len(questions)-1)
    third = input(f"{questions[random_question]}\n")

    # what is your favoirte color
    if random_question == 0:
        if third in answers:
            print("You have been  cast into the gorge!! \n"
            )
            return False
        else:
            answers.append(thrid)
            print("Right. off you go. \n")
            return True
    # what it the speed of an african swallow
    elif random_question == 1:
        if third == correct_answer:
            print("WAIT...I don't know... AHHH \n the bridge keeper was cast into the gorge.")
            return False    
        else:
            print("You have been cast into the gorge")
            return False  
    
    #what is the capital of Assyria
    elif random_question == 2:
        if third == "Ninevah":
            print("right then off you go")
            return True
        else:
            print("you've been cast into the gorge")
            return False
isGuessing = bridge_keeper()

while isGuessing == True:
    isGuessing == bridge_keeper()
        