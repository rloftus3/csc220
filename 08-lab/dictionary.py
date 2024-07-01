#!/usr/local/bin/python3
from pprint import pprint
import csc220
csc220.showForm("<br/>")

def name(parts):
    print("Rachel Loftus")

def dump(parts):
    global dictionary
    pprint(dictionary)

def assign(args):
    global dictionary
    key = args[0]
    val = args[2]

    if val[0] in "1234567890":
        dictionary[key] = val
    elif val[0] in "qwertyuiopasdfghjklzxcvbnm":
        if val not in dictionary:
            raise UserWarning(f"ERROR: {' '.join(args)}")
        val = dictionary[val]
        dictionary[key] = val
    else:
        raise UserWarning(f"ERROR: {' '.join(args)}")

data = csc220.getInput('textarea')
lines = data.split('\n')
dictionary = {}
command = {
    "DUMP": dump, 
    "NAME": name, 
    "<-": assign
}

print("<pre>")
for line in lines:
    parts = line.split()
    count = len(parts)

    if count == 1:
        func = command[parts[0]]
    elif count == 3:
        func = command[parts[1]]
    else:
        raise UserWarning(f"ERROR: {line}")

    print(f"<{func} {parts}>")
    func(parts)
print("</pre>")
 
# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!