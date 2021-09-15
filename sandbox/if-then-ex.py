"""Challenge Question #1"""

choice: int = int(input("Enter a Number: "))


if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")



#My work is below for my attempt on the challenge
"""
if choice < 50:
    if choice <= 25:
        print("A")
    else:
        print("B")
else: 
    if choice >= 75: 
        print("C")
    else:
        print("D")
"""