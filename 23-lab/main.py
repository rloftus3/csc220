#!/usr/local/bin/python3
import csc220
import graph
import mst
from tabulate import tabulate
csc220.showForm("<br/>")

def MST_print(tree, message):
    counter = 0
    table = [["Edge"]]
    for e in tree:
        table.append([e])
        counter = counter + e.element()
    html_table = tabulate(table, headers = "firstrow", tablefmt = "unsafehtml")
    # print html table output
    print(f"<div> <h2>{message}</h2> {html_table} </div>")
    print(f"<div> <b>Total Weight: {counter}</b> </div>")

# get graph data
data = csc220.getInput('textarea')
lines = data.split('\n')
g = graph.Graph(False)
vNames = []
eNames = []
foundEdges = False

# process data; split into verts, edges, and weights
for raw_line in lines:
    line = raw_line.strip()
    if line == "#end":
        foundEdges = True
        continue
    if len(line) < 1:
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
        parent = verts[parts[0]]
        child = verts[parts[1]]
        weight = float(parts[2])
    except KeyError as e:
        continue
    else:
        g.insert_edge(parent, child, weight)

# build table structure for output
table = [["Parent", "Child", "Weight"]]
for v in g.vertices():
    parent = v.element()
    for e in g.incident_edges(v, outgoing=True):
        child = e.opposite(v).element()
        weight = e.element()
        table.append([parent, child, weight])
html_table = tabulate(table, headers = "firstrow", tablefmt = "html")

# print html table output
print(f"<div> <h2>Your Graph</h2> {html_table} </div>")

# run Kruskal and output MST & total weight
K_counter = 0
K_tree = mst.MST_Kruskal(g)
MST_print(K_tree, "Kruskal's MST")

# run Prims and output MST & total weight
P_counter = 0
P_tree = mst.MST_PrimJarnik(g)
MST_print(P_tree, "Prim's MST")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus