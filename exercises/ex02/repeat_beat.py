"""Repeating a beat in a loop."""

__author__ = "730484925"
i: int = 0
beat: str = input("What beat do you want to repeat?")
repeat: str = input("How any times do you want to repeat it?")
repeat_int: int = int(repeat)
print_beat: str = beat
if repeat_int <= 0:
    print("No beat...")
else:
    while i < repeat_int:
        print_beat = print_beat + " " + beat
        i = i + 1
    print(print_beat)       

