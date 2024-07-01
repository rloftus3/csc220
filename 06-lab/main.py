import quicksort
from random import randint

# Generating a list with random size and variables
def randList(size, min, max):
    return list(randint(min, max) for i in range(size))

# Testing quick sort
# data = [2, 3, 4, 5, 7]
# quicksort.inplace_quick_sort(data, 0, len(data) - 1)
# print(quicksort.listVisits)

for i in range(300):
    size = randint(10000, 20000)
    thelist = randList(size, 0, 99999)
    quicksort.inplace_quick_sort(thelist, 0, len(thelist) - 1)
    print(f"{size}, {quicksort.listVisits}")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!