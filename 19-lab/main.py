#!/usr/local/bin/python3
import csc220
import graph
from tabulate import tabulate
csc220.showForm("<br/>")

data = csc220.getInput('textarea')
lines = data.split('\n')
g = graph.Graph(True)
vNames = []
eNames = []
foundEdges = False

for line in lines:
  if line == "#end":
      foundEdges = True
      continue
  if foundEdges:
    eNames.append(line)
  else:
    vNames.append(line)

verts = {}
for vName in vNames:
  verts[vName] = g.insert_vertex(vName)
for eName in eNames:
  parts = eName.split(', ')
  v1 = verts[parts[0]]
  v2 = verts[parts[1]]
  g.insert_edge(v1, v2)

# build table structure for output
table = [["Vertex", "Outgoing Edges"]]

for v in g.vertices():
  # print(v.element())
  edges = []
  for e in g.incident_edges(v, outgoing=True):
    # v2 = e.opposite(v)
    # print(f"Points at: {v2}")
    edges.append(e.opposite(v))
  table.append([v.element(), edges])
html_table = tabulate(table, headers = "firstrow", tablefmt = "html")

# print html table output
print(f"<div> {html_table} </div>")



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus