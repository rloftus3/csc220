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
    print(f"Enter {win(pos)}")
    return pos == lastCell

def tooHigh(pos): 
    global lastCell
    print(f"Enter {tooHigh(pos)}")
    return pos > lastCell

def tooLow(pos):
    print(f"Enter {tooLow(pos)}")
    return pos < 0

def valZero(pos):
    global board
    print(f"Enter {valZero(pos)}")
    return board[pos] != 0 # Need function to return False to indicate win is impossible

def alreadyVisited(pos):
    global visits
    return pos in visits

def canWin(pos):
    print(f"Enter {canWin(pos)}")
    rv = True
    global board
    global winningPath
    global visits

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
        winningPath.append(pos) 
        if canWin(pos - board[pos]) or canWin(pos + board[pos]):
            rv = True
        else:
            rv = False
    print(f"Exit {canWin(pos)}")
    return rv
    
# Turning space-separated input into list of integers
dataMap = map(int, data.split())
board = list(dataMap)
lastCell = len(board) - 1

# Playing the game
print(f"Board: {board}")
if canWin(0):
    print(f"Winning path: {winningPath}")
else:
    print(f"No winning path.")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!