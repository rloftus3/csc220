#!/usr/local/bin/python3
import csc220
from kmp import *
# csc220.showForm("This is the comment on the form area.")  
haystack = csc220.getInput('textarea')
needle = csc220.getInput('textbox')

pos = KMPmatch(needle, haystack)

if pos >= 0:
    print(f"The position of the first character of {needle} is: {pos}.")
else:
    print(f"{needle} is not contained within your input.")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus