import numpy as np
#int zeroes for custom grid width/height ?
def Init(rows, columns):
    return np.zeros ((rows, columns))

def Life(grid, rows, columns):
    for i in range(rows):
        for j in range(columns):
            CheckRules(grid, rows, columns, i, j)
    for i in range(rows):
        for j in range(columns):
            ApplyRules(grid, i, j)
    print("Applied Rules")

def CheckRules(grid, rows, columns, x, y):
    # Count live cells adjacent to current cell
    # print("")
    # print("Coord: " + str(x) + "," + str(y))
    adjCnt = 0
    for i in range(x-1, x+2):
        if(0 <= i < rows):
            for j in range (y-1, y+2):
                if(0 <= j < columns):
                    # print("i: " + str(i) + " j: " + str(j))
                    # print("grid[i][j]: " + str(grid[i][j]))
                    # print("x != i: " + str(x != i))
                    # print("y != j: " + str(y != j))
                    # print("x != i and y != j: " + str(x != i or y != j))
                    if (grid[i][j] == 2 or grid[i][j] == 3) and (x != i or y != j) :
                        adjCnt += 1
                        #print("adjcnt++: " + str(adjCnt))

    # Any live cell with 2 or 3 neighbors survives
    # Any dead cell with three live neighbors becomes a live cell
    # All other live cells die.
    # aka
    # If the current cell is dead and has 3 adjacent ones alive, it lives
    # or if the current cell is alive but does not have 2 or 3 live neighbors, it dies
    # else nothing changes

    # 1 = dead
    # 2 = alive
    # 3 = marked to die
    # 4 = marked to live

    if grid[x][y] == 1 and adjCnt == 3:
        grid[x][y] = 4
    elif grid[x][y] == 2 and (adjCnt < 2 or adjCnt > 3):
        grid[x][y] = 3
    else:
        pass

def ApplyRules(grid, x, y):
    # change all 3's to 1, and all 4's to 2
    if grid[x][y] >= 3:
        grid[x][y] -= 2

# following functions mostly used for testing

def life_run():
    # rows = int(input("Enter the rows in the grid: "))
    # columns = int(input("Enter the columns in the grid: "))
    # grid = Init(rows, columns)

    # to be implemented: signify points manually, probably will just add a ui for ease of testing
    # cellsAlive = [(2,3)]

    rows = 17
    columns = 17

    grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1],
            [1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1],
            [1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,1,1,2,2,1,2,2,1,1,2,2,2,1],
            [1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1],
            [1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1],
            [1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1],
            [1,2,2,2,1,1,2,2,1,2,2,1,1,2,2,2,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1],
            [1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1],
            [1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]

    print("First Generation")
    Display(grid, rows, columns)

    for i in range(5):
        Life(grid, rows, columns)
        Display(grid, rows, columns)

def Display(grid, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if(int(grid[i][j]) == 1):
                print(' ', end ='  ' , flush=True)
            elif(int(grid[i][j]) == 2):
                print('*', end = '  ')
        print()


if __name__ == '__main__':
    life_run()