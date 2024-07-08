#!/usr/local/bin/python3
import csc220
import avl_tree
import pprint
csc220.showForm("This is the comment on the form area.")  
data = csc220.getInput('textarea')

myMap = avl_tree.AVLTreeMap()

# filename = "/home/staff/kurban/public/lists/web2.txt"
filename = "web2.txt"
with open(filename, "r") as dictFile:
    for line in dictFile:
        word = line.strip().lower()
        if len(word) > 0:
            myMap[word] = None

misspelledWords = []
lines = data.split("\n")
for line in lines:
    words = line.split()
    for word in words:
        word = word.lower()
        if word not in myMap:
            misspelledWords.append(word)
    
print(f"Misspelled Words: {misspelledWords}")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus