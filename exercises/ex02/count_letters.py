"""Counting letters in a string."""

__author__ = "730484925"

alpha_counter: int = 0
letter: str = input("What letter do you want to search for?:")
word: str = input("Enter a word:")
i: int = 0
#letter_checker: str = None
while i < len(word):
    letter_checker = word[i]
    if letter_checker == letter:
        alpha_counter = alpha_counter + 1
    i = i + 1
print("Count: " + str(alpha_counter))