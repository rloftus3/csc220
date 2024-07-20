#!/usr/local/bin/python3
import csc220
import graph
import dfs
from tabulate import tabulate
csc220.showForm("<br/>")

# get data
data = csc220.getInput('textarea')
lines = data.split('\n')
g = graph.Graph(True)
vNames = []
eNames = []
foundEdges = False

# process data; split in verts and edges
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

in_progress = []
finished = []
cycle_found = False

for v in g.vertices():
    if v not in in_progress or v not in finished:
        # print(f"First call to DFS_cycle, in progress: {in_progress}")
        cycle_found = dfs.DFS_cycle(g, v, in_progress, finished)
    if cycle_found:
        break
if g.vertex_count() > 1:
    if cycle_found:
        message = "This graph is cyclic!"
    else:
        message = "This graph is acyclic!"
    print(f"<div> {message} </div>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus