import numpy as np

rows = 5
columns = 5
# columns = int(input("Enter the columns in the grid: "))
# grid = Init(rows, columns)

cellsAlive = [(2,3)]

def Main():
    global rows
    global columns

    rows = int(input("Enter the rows in the grid: "))

    grid = [[0,0,0,0,0],
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

    print("First Generation")
    Display(grid, rows, columns)
    Life(grid, rows, columns)
    Display(grid, rows, columns)



def Init(rows, columns):
    return np.zeros ((rows, columns))

def Display(grid, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(int(grid[i][j]), end ="" , flush=True),
        print("")

def Life(grid, rows, columns):
    for i in range(rows):
        for j in range(columns):
            CheckRules(grid, i, j)
    print("Checked Rules")
    Display(grid, rows, columns)
    for i in range(rows):
        for j in range(columns):
            ApplyRules(grid, i, j)
    print("Applied Rules")

def CheckRules(grid, x, y):
    global rows
    global columns
    # Count live cells adjacent to current cell
    print("Coord: " + str(x) + "," + str(y))
    adjCnt = 0
    for i in range(x-1, x+2):
        if(0 < i < x):
            for j in range (y-1, y+2):
                print("i: " + str(i))
                print("j: " + str(j))
                if (grid[i][j] == 1 or grid[i][j] == 2) and (x != i and y != j) :
                    adjCnt += 1
                    print("adjcnt++: " + str(adjCnt))

    # Any live cell with 2 or 3 neighbors survives
    # Any dead cell with three live neighbors becomes a live cell
    # All other live cells die.
    # aka
    # If the current cell is dead and has 3 adjacent ones alive, it lives
    # or if the current cell is alive but does not have 2 or 3 live neighbors, it dies
    # else nothing changes

    # 0 = dead
    # 1 = alive
    # 2 = marked to die
    # 3 = marked to live

    if grid[x][y] == 0 and adjCnt == 3:
        print(adjCnt)
        grid[x][y] = 3
    elif grid[x][y] == 1 and (adjCnt < 2 or adjCnt > 3):
        print(adjCnt)
        grid[x][y] = 2
    else:
        pass

def ApplyRules(grid, x, y):
    # change all 2's to 0, and all 3's to 1
    if grid[x][y] == 2:
        grid[x][y] = 0
    elif grid[x][y] == 3:
        grid[x][y] = 1
    else:
        pass

Main()