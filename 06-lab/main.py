import quicksort
from random import randint

# Generating a list with random size and variables
def randList(size, min, max):
    return list(randint(min, max) for i in range(size))

