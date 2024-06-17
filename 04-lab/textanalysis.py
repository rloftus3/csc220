#!/usr/local/bin/python3
from statistics import mean
import csc220
csc220.showForm("This is the comment on the form area.")  
data = csc220.getInput('textarea')

strings = data.split()
dataSize = len(strings)

# Counting words in input; if there are less than 100, exit
print(f"<p>The number of words in this input is: {dataSize}</p>")
if dataSize < 100:
    print(f"<p>Hey, Dude, that's too small a paragraph. Try again with something longer.</p>")
    # exit()

print("Hello!")
# Calculate average length of string via list comprehension
wordLengths = [len(s) for s in strings]
avg = mean(wordLengths)

print(f"<p>The average length of each string is: {avg}</p>")

# Sort into lexographical order...
# Sorted in place, thus no need for variable assignment
strings.sort()
itr = dataSize // 10

# ...and print into 10x10 grid
for i in range(itr):
    start = i * 10
    print(f"<p> {strings[start : start+10]} </p>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!