###########################################
#            Daily Programmer             #
# Challenge #165 Easy: ASCII Game of Life #
#              June 5 2014                #
###########################################

grid = []
neighbourCoord = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

with open('165_easy_input.txt', 'r') as f:
    N, X, Y = map(int, f.readline().split(' '))
    grid = f.read().split('\n')

def readPos(pos):
    xPos, yPos = pos
    xPos %= X
    yPos %= Y

    if(grid[yPos][xPos] == '#'):
        return True
    else:
        return False

def neighbours(pos):
    sumNeighbours = 0
    for coord in neighbourCoord:
        if (readPos(map(sum, zip(pos, coord)))):
            sumNeighbours += 1
    return sumNeighbours


for i in range(N):
    newGrid = []
    for yPos in range(Y):
        newGrid.append("")
        for xPos in range(X):
            neighboursAtPos = neighbours((xPos,yPos))
            if (readPos((xPos,yPos))): # Point is alive
                if (neighboursAtPos < 2 or neighboursAtPos > 3): # Under or overpopulation
                    newGrid[yPos] += "." # Become dead
                else:
                    newGrid[yPos] += "#" # Remain alive
            else: # Point is dead
                if (neighboursAtPos == 3):
                    newGrid[yPos] += '#' # Become alive
                else:
                    newGrid[yPos] += "." # Remain dead
    grid = newGrid

printString = ""

for line in grid:
    print line