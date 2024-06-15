#!/usr/local/bin/python3
import sys
from random import randint
sys.path.append('/home/staff/kurban/python')
import csc220
import circle
import color
import point

# code that creates 1000 or so objects and puts them in circle_list
# that code will generate Point and Color objects to build the circles

def rand_point():
    return (randint(0, 1000), randint(0, 1000))

def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

circle_list = []

for count in range(0, 1000):
    p = point.Point(*rand_point())
    r = randint(2, 50)
    f = color.Color(*rand_color())
    circle_list.append(circle.Circle(p, r, f))


print ('<svg height="1000" width="1000">')
for c in circle_list:
    print(c.html())
print ('</svg>')   



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus 
# there is nothing below here!