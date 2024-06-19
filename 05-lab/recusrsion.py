#!/usr/local/bin/python3
import csc220
csc220.showForm("This game uses the text area, not the text box.")  
data = csc220.getInput('textarea')

# Lists to keep track of spaces visited
visits = []
winningPath = []
board = []

# Functions return Boolean values to check if path leads to a win
def win(pos):
    global lastCell
    return pos == lastCell

def tooHigh(pos): 
    global lastCell
    return pos > lastCell

def tooLow(pos):
    return pos < 0

def valZero(pos):
    global board
    return board[pos] == 0 

def alreadyVisited(pos):
    global visits
    return pos in visits

def canWin(pos):
    global board
    global visits
    global winningPath
    rv = True

    if win(pos):
        winningPath.append(pos)
        return True
    if tooHigh(pos):
        rv = False
    elif tooLow(pos):
        rv = False
    elif valZero(pos):
        rv = False
    elif alreadyVisited(pos):
        rv = False
    visits.append(pos)
    if rv:
        if canWin(pos - board[pos]) or canWin(pos + board[pos]):
            rv = True
            winningPath.append(pos)
        else:
            rv = False
    return rv
    
# Turning space-separated input into list of integers
dataMap = map(int, data.split())
board = list(dataMap)
lastCell = len(board) - 1

# Playing the game
print(f"Board: {board}")
print()
if canWin(0):
    winningPath.reverse()
    print(f"Winning path: {winningPath}")
else:
    print(f"No winning path.")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!