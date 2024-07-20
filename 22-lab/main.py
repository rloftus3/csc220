#!/usr/local/bin/python3
import csc220
import graph
from tabulate import tabulate
csc220.showForm("<br/>")

# get data
data = csc220.getInput('textarea')
lines = data.split('\n')
g = graph.Graph(True)
vNames = []
eNames = []
foundEdges = False

# process data; split into verts, edges, and weights
for line in lines:
    if line == "#end":
        foundEdges = True
        continue
    if foundEdges:
        eNames.append(line)
    else:
        vNames.append(line)

# building graph
verts = {}
for vName in vNames:
    if vName in verts:
        continue
    verts[vName] = g.insert_vertex(vName)
for eName in eNames:
    parts = eName.split(', ')
    try:
        v1 = verts[parts[0]]
        v2 = verts[parts[1]]
    except KeyError as e:
        # print(f"Invalid endpoint: {e}.") 
        continue
    else:
        g.insert_edge(v1, v2)

# build table structure for output
table = [["Vertex", "Outgoing Edges"]]
for v in g.vertices():
    edges = []
    for e in g.incident_edges(v, outgoing=True):
        edges.append(e.opposite(v).element())
    table.append([v.element(), "<br/>".join(edges)])
html_table = tabulate(table, headers = "firstrow", tablefmt = "unsafehtml")

# print html table output
print(f"<div> {html_table} </div>")



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus