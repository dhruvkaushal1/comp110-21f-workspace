"""Project for creating your own battle adventure."""
from random import randint
import time

__author__: str = "730484925"

cow_type: str = ""
cow_health: int = 0 
player: str = ""
points: int 
points = cow_health
cow_emoji: str = "\U0001F42E"
round: int = 1


def main() -> None:
    """This is the main function to choose whether you would like to play the hard version, easy version, or quit."""
    greet()
    global cow_health
    global round
    while round > 0:
        boss_level: str = input("What boss would you like to vs: Easy Boss, Hard Boss, or quit? ")
        if boss_level == "Easy Boss":
            easy_boss()
        elif boss_level == "Hard Boss":
            cow_health = hard_boss(cow_health)
        else:
            done()
            round -= 1
        if (input("Would you like to play again? ")) != "yes":
            round -= 1


def greet() -> None:
    """This greet function is used to assign the player a name and give the player a random cow with each having differnt health points."""
    global player
    player = input("Type Your Player Name: ")
    print(f"Hello, {player}, you are now going to embark on a \njourney where you will battle tyrants of our world")
    print("Now, you will be bestowed a creature from our world!\n")
    time.sleep(7)
    cow_number: int = randint(1, 3)
    if cow_number == 1:
        global cow_type
        global cow_health
        cow_type = "Sky Cow"
        cow_health = 75
    elif cow_number == 2:
        cow_type = "Land Cow"
        cow_health = 125
    else: 
        cow_type = "Sea Cow"
        cow_health = 100
    print(f"You have been given the {cow_type} {cow_emoji} by the guardians of our world!! \n\nGo on and fulfill your fate to become the protector of world \nThis is where LEGENDS are made...")
    print(cow_emoji)
    

def easy_boss() -> None:
    """Easy boss is a simple attack based boss which is easy to beat."""
    print("Your first boss is the nefarious Electric Giraffe!!! \nThe Electric Giraffe has taken a hold over our land's electrical grid and takes away all our power \nWe need your help to take him down!")
    electirc_giraffe_health: int = 100
    print("Your Battle has begun. Enter the attacks and defenses that you would like to use when asked")
    print(cow_emoji)
    attack_one: str = input("Would you like to use headbutt or supersonic? ")
    if attack_one == "supersonic":
        electirc_giraffe_health = electirc_giraffe_health - 40
        print(f"Girraffe Health: {electirc_giraffe_health}")
    else:
        electirc_giraffe_health = electirc_giraffe_health - 25
        print(f"Girraffe Health: {electirc_giraffe_health}")
    defense_one: str = input("Would you like to use time shield, or light shield? ") 
    if defense_one == "time shield":
        print(f"{player}, giraffes are clearly impervious to time control in our realm \n Electric Giraffe's attack was not blocked!!")
        global cow_health
        cow_health = cow_health - 20
        print(f"Cow Health: {cow_health}")
    else:
        print("Good choice, Electric Giraffe's attack was blocked!!")
    attack_two: str = input("Would you like to use super slap, or milk attack? ")
    if attack_two == "super slap":
        electirc_giraffe_health = electirc_giraffe_health - 80
        print(f"Girraffe Health: {electirc_giraffe_health}")
    else: 
        electirc_giraffe_health = electirc_giraffe_health - 100
        print(f"Girraffe Health: {electirc_giraffe_health}")
    if electirc_giraffe_health < 0:
        print("Wow you annihilated the Electric Giraffe")
    print(f"{player} you have defeated the horrible, Electric Giraffe")
    print(f"Your score for this round is {cow_health}")
    print(cow_emoji)


def hard_boss(hardhealth: int) -> int:
    """Hard boss takes a longer time than easy boss and incorporates a random variable within defense."""
    global player
    print("Your boss is the villinaous fire rhino!!! \n The Fire Rhino has been the tyrant of our land for so long. \nHe is the boss of all of the crminals")
    print(f"Taking him on is not going to be an easy challenge, but, {player}, You can do it!!!")
    print("Your Battle has begun. Enter the attacks and defenses that you would like to use when asked")
    print(cow_emoji)
    fire_rhino_health: int = 150
    global cow_type
    attack_one: str = input("Would you like to use brave cow or cow beam? ")
    if attack_one == "brave cow":
        fire_rhino_health = fire_rhino_health - 20
        print(f"Fire Rhino Health: {fire_rhino_health}")
    else:
        fire_rhino_health = fire_rhino_health - 15
        print(f"Fire Rhino Health: {fire_rhino_health}")
    defense_one: str = input("Would you like to use milk shield, or grass defense? ") 
    if defense_one == "milk shield":
        print("Fire Rhino's core temperature evaporated all of the liquid!! \nFire Rhino's attack was not blocked")
        hardhealth = hardhealth - 20
        print(f"Cow Health: {hardhealth}")
    else:
        print(f"The Grass was set ablaze by Fire Rhino's fire attack!! \nThis caused extra burn on your, {cow_type}")
        hardhealth = hardhealth - 40
        print(f"Cow Health: {hardhealth}")
    attack_two: str = input("Would you like to use cow tail or outrage? ")
    if attack_two == "cow tail":
        fire_rhino_health = fire_rhino_health - 25
        print(f"Fire Rhino Health: {fire_rhino_health}")
    else: 
        fire_rhino_health = fire_rhino_health - 35
        print(f"Fire Rhino Health: {fire_rhino_health}")
    defense_two: str = input("Would you like to use cotton guard or ice shield? ") 
    critical_hit: int = randint(1, 6)
    if critical_hit < 3:
        print(f"No Good, {player}, your defense failed")
        hardhealth = hardhealth - 40
    elif defense_two == "ice shield":
        print("Good Choice!! The ice Nullifed Fire Rhino's attack \nFire Rhino's attack was blocked")
        print(f"Cow Health: {hardhealth}")
    else:
        print(f"The Cotton was set ablaze by Fire Rhino's fire attack!! \nThis caused extra burn on your, {cow_type}")
        hardhealth = hardhealth - 40
        print(f"Cow Health: {hardhealth}")
    print("\n\n *A bright shining light appears in the sky. It calls to you.\nYou let it come to you and open your hand naturally\n In a blinding light, you are left with a stone in your hand*")
    print("The stone has a moon on it\n\n")
    print("This is a power up moonstone, you have been given the choice of a special attack that will have a 3x multiplier")
    attack_three: str = input("\n\nWould you like to use multi shadow cow or cow flash super circle dance?")
    if attack_three == "multi shadow cow":
        hardhealth = hardhealth - 25
        print("Recoil from the attack lowered your cow's health")
        print("Fire Rhino Health: 0")
    else:
        hardhealth = hardhealth - 20
        print("Recoil from the attack lowered your cow's health")
    print(f"{player} you have defeated the horrible Fire Rhino")
    print(f"Your score for this round is {hardhealth}")
    return hardhealth


def done() -> None:
    """This function ends the game if the player would like to end from the beginning of the program."""
    global cow_health
    print(f"Your score is: {cow_health}")
    print("Thank you for playing. We will see you next time.")
    print(cow_emoji)
    

if __name__ == "__main__":  
    main() 