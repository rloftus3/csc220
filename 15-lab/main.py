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
    lines = data.split('\n')
    for line in lines:
        word = line.strip()
        myMap[word] = None


misspelledWords = []
keys = [ k for k in myMap.keys() ]
lines = data.split("\n")
for line in lines:
    # pprint.pprint(line)
    words = line.split()
    for word in words:
        pprint.pprint(word)
        if word not in keys:
            misspelledWords.append(word)
    
print(misspelledWords)

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus