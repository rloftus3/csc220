#!/usr/local/bin/python3
from pprint import pprint
import csc220
import expressiontree
csc220.showForm("<br/>")

def name(parts):
    print("Rachel Loftus")

def dump(parts):
    global varTable
    pprint(varTable)

def replaceVar(val):
    if val[0] in "qwertyuiopasdfghjklzxcvbnm":
        if val not in varTable:
            raise UserWarning(f"ERROR: val '{val}' not in varTable.")
        val = varTable[val]
    return str(val)

def assign(args):
    global varTable
    key = args[0]
    rawExpr = args[2:]
    # pprint(rawExpr)
    filteredExpr = [ x for x in map(replaceVar, rawExpr) ]
    pprint(filteredExpr)
    etree = expressiontree.build_expression_tree(filteredExpr)
    val = etree.evaluate()
    varTable[key] = val

data = csc220.getInput('textarea')
lines = data.split('\n')
varTable = {}
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
    else:
        func = command[parts[1]]

    print(f"DEBUG: <{func} {parts}>")
    func(parts)
print("</pre>")
 
# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!