#!/usr/local/bin/python3
import csc220
from heap_priority_queue import HeapPriorityQueue
from tabulate import tabulate
import pprint

csc220.showForm("This is the comment on the form area.")  
data = csc220.getInput('textarea')
freqs = {}
pq = HeapPriorityQueue()
huffman = {}

# get freq of every ch in data
for ch in data:
    freqs[ch] = freqs.get(ch, 0) + 1

# create pq keyed on freqs of each ch
for ch,freq in freqs.items():
    pq.add(freq, ch)

# prepopulate code map with characters
huffman = {ch:"" for ch in freqs}

# build Huffman code map
while len(pq) > 1:
    freq1, ch1 = pq.remove_min()
    freq2, ch2 = pq.remove_min()
    combined = (freq1 + freq2, ch1 + ch2)
    pq.add(*combined)
    for k in ch1:
        huffman[k] = "0" + huffman[k]
    for k in ch2:
        huffman[k] = "1" + huffman[k]

# build table structure for output
table = [["Character", "Frequency", "Possible Huffman Code"]]
for char in huffman:
    table.append([ch, freqs[ch], huffman[ch]])
html_table = tabulate(table, headers = "firstrow", tablefmt = "html")

# print html table output
print(f"<div> {html_table} </div>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus