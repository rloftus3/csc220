#!/usr/local/bin/python3
import sys
from statistics import mean
sys.path.append('/home/staff/kurban/python')
import csc220
csc220.showForm("This is the comment on the form area.")  
data = csc220.getInput('textarea')

strings = data.split()
dataSize = len(strings)

# Counting words in input; if there are less than 100, exit
print(f"<p>The number of words in this input is: {dataSize}</p>")
if dataSize < 100:
    print(f"<p>Hey, Dude, that's too small a paragraph. Try again with something longer.</p>")
    exit()

# Calculate average length of string
avg = mean(strings)
print(f"<p>The average length of each string is: {avg}</p>")

# Sort into lexographical order...
strings.sorted()
itr = dataSize / 10

# ...and print into 10x10 grid
print("<p>")
for i in range(itr):
    start = i * 10
    print(strings[start:start + 10])
print("</p>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!