#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')
import csc220

def circleLeft():
    return """
    <circle cx="50" cy="500" r="40" stroke="green" stroke-width="10" fill="white" />
    """
def circleRight():
    return """
    <circle cx="950" cy="500" r="40" stroke="red" stroke-width="5" fill="white" />
    """
def rectangle():
    return """
    <rect width="200" height="100" x="400" y="480" fill="navy" />
    """

def name():
    return """
    <text x="480" y="535" fill="white">Rachel</text>
    """

print('<svg height="1000" width="1000">')
print(circleLeft())
print(circleRight())
print(rectangle())
print(name())
print('</svg>')



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus 
# there is nothing below here!