"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730484925"
from random import randint
fortune_number: int = (randint(1, 4))
print("Your fortune cookie says...")
if fortune_number == 1:
    print("A beautiful, smart, and loving person will be coming into you life")
else:
    if fortune_number == 2:
        print("Something bad will happen to your shoes today")
    else:
        if fortune_number == 3:
            print("Something good will happen to you today")
        else:
            if fortune_number == 4:
             print("You are going to be extremly happy tonight!")
print("Now, go spread positive vibes!") 