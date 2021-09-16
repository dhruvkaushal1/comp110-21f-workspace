"""Finding duplicate letters in a word."""

__author__ = "730484925"
word: str = input("Enter a word: ")
i: int = 0
j: int = i + 1
letter: str 
duplicate: str
same: bool = False
while i < len(word):
    letter = word[i]
    j = i + 1
    while j < len(word):
        duplicate = word[j]
        j += 1
        if (duplicate == letter):
            same = True
    i += 1
print("Found duplicate: " + str(same))