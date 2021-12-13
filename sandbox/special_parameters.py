"""Examples of optional parameters and union types."""

from typing import Union

def hello(name: Union[str, int, float] = "World", times: int = 1) -> str:
    "Fun reading."
    greeting: str = "Hello"
    if isinstance(name, str):
        greeting: str = "Hello, " + name
    elif isinstance(name, int):
        greeting += "COMP " + str(name)
    else:
        greeting += "Aline Life from SEctor " + str(name)
    return greeting

#Single-Argument
print(hello("Sally"))

#No Arguments
print(hello())


# int ARgument works as well
print(hello(110))


print(hello(3.14))