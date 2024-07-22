#!/usr/local/bin/python3
import csc220
import graph
import dfs
import shortest_paths
import pprint
from tabulate import tabulate
csc220.showForm("<br/>")

# get data
data = csc220.getInput('textarea')
lines = data.split('\n')
g = graph.Graph(True)
vNames = []
eNames = []
foundEdges = False

# EXTRA: get textbox data
raw_textbox = csc220.getInput('textbox')
textbox = raw_textbox.strip()
parts = textbox.split(', ')
v_start = parts[0]
v_end = parts[1]

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
# edges = {}
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
        # print(f"Invalid endpoint: {e}.") 
        continue
    else:
        g.insert_edge(parent, child, weight)
        # edges[f"{parent}, {child}"] = weight

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
# print(f"<div> <h2>Your Graph</h2> {html_table} </div>")

# run dijkstra to find all shortest paths from v_start and associated weights
distanceMap = shortest_paths.shortest_path_lengths(g, verts[v_start])
tree_edges = shortest_paths.shortest_path_tree(g, verts[v_start], distanceMap)

# convert to strings
paths = {}
for v,e in tree_edges.items():
    vName = v.element()
    parent, child = (v.element() for v in e.endpoints())
    weight = e.element()
    paths[vName] = (parent, child, weight)

# finding actual path from v_start to v_end
notDone = True
pathFound = False
parent = v_end
cost = 0
martin_short_est_path = []

while notDone:
    try:
        martin_short_est_path.append(paths[parent])
    except KeyError:
        notDone = False
    else:
        parent, child, weight = martin_short_est_path[-1]
        cost = cost + weight
    if parent == v_start: 
        notDone = False
        pathFound = True

# output shortest path
if pathFound:
    table2 = [["Edge", "Weight"]]
    for i in range(len(martin_short_est_path) - 1, -1, -1):
        parent, child, weight = martin_short_est_path[i]
        table2.append([f"{parent} &rarr; {child}",  weight])
    html_table2 = tabulate(table2, headers = "firstrow", tablefmt = "html")
    # print html table output
    print(f"<div> <h2>Shortest Path</h2> {html_table2} </div>")
    print(f"<div> <b>Total Weight: {cost}</b> </div>")
else:
    print("<div> No path found. </div>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus