from random import randint

# Generating a list with random size and variables
def randList(size, min, max):
    return list(randint(min, max) for i in range(size))    

# Insertion sort in Python
def insertionSort(thelist):
    listVisits = 0
    for i in range(1,len(thelist)):
        value = thelist[i]
        j = i - 1
        while j >= 0:
            if value < thelist[j]:
                lessThan = True
            else:
                lessThan = False
            listVisits += 1
            if lessThan == True:
                thelist[j + 1] = thelist[j]
                thelist[j] = value
                j = j - 1
            else:
                break
    return listVisits

# Testing insertion sort
# data = [9, 5, 1, 4, 3]
# insertionSort(data)

for i in range(300):
    size = randint(1000, 5000)
    thelist = randList(size, 0, 99)
    listVisits = insertionSort(thelist)
    print(f"{size}, {listVisits}")


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!