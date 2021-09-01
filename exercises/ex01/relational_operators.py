"""Using different input types to apply relational operators"""
__author__ = "730484925"

leftside: str = input("Left-hand side: ")
rightside: str = input("Right-hand side: ")
leftside_int: int = int(leftside)
rightside_int: int = int(rightside)
print(leftside + " < " + rightside + " is " + str(leftside_int < rightside_int))
print(leftside + " >= " + rightside + " is " + str(leftside_int >= rightside_int))
print(leftside + " == " + rightside + " is " + str(leftside_int == rightside_int))
print(leftside + " != " + rightside + " is " + str(leftside_int != rightside_int))
