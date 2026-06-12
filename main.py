import copy

# We can add parameters to specify what the grid should look like later
def create_grid():
    # Create 9x12 grid (each element initialised with empty string)
    grid = [[""] * 9 for _ in range(12)]

    faces = [
        ["w", 3, 5, 0, 2],
        ["b", 3, 5, 3, 5],
        ["y", 3, 5, 6, 8],
        ["g", 3, 5, 9, 11],
        ["r", 0, 2, 3, 5],
        ["o", 6, 8, 3, 5]
    ]

    for face in faces:
        for i in range(face[3], face[4] + 1):
            for j in range(face[1], face[2] + 1):
                grid[i][j] = face[0]

    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def R(grid):
    col = [grid[i][5] for i in range(12)]
    for i in range(12): 
        grid[i][5] = col[(i+3) % 12]
    
    for i in range(3):
        for j in range(3):
            grid[i+3][j+6] = grid[(j%6)+3][8-(i%3)]

    return grid

def RP(grid):
    return R(R(R(grid)))

def L(grid):
    col = [grid[i][3] for i in range(12)]
    for i in range(12):
        grid[i][3] = col[(i-3) % 12]
    
    for i in range(3):
        for j in range(3):
            grid[i+3][j] = grid[(j%3)+3][i]

    return grid

def LP(grid):
    return L(L(L(grid)))

def F(grid):
    gridcopy = copy.deepcopy(grid)
    
    row = [grid[5][i] for i in range(9)]
    for i in range(9):
        grid[5][i] = row[(i-3) % 9]

    for i in range(3):
        grid[5][i] = gridcopy[9][i+3]
        grid[9][i+3] = gridcopy[5][8-i]
        for j in range(3):
            grid[i+6][j+3] = grid[8-(j%3)][i+3]

    return grid

def FP(grid):
    return F(F(F(grid)))

def B(grid):
    gridcopy = copy.deepcopy(grid)

    row = [grid[3][i] for i in range(9)]
    for i in range(9):
        grid[3][i] = row[(i+3) % 9]

    for i in range(3):
        grid[3][i+6] = gridcopy[11][5-i]
        grid[11][i+3] = gridcopy[3][2-i]
        for j in range(3):
            grid[i+6][j+3] = grid[8-(j%3)][i+3]

    return grid

def BP(grid):
    return B(B(B(grid)))

def U(grid):
    gridcopy = copy.deepcopy(grid)

    for i in range(3):
        grid[2][i+3] = gridcopy[5-(i%3)][6]
        grid[i+3][2] = gridcopy[2][5-(i%3)]
        grid[6][i+3] = gridcopy[5-(i%3)][2]
        grid[i+3][6] = gridcopy[6][5-(i%3)]
        for j in range(3):
            grid[i+3][j+3] = gridcopy[j+3][5-(i%3)]

    return grid

def UP(grid):
    return U(U(U(grid)))

def D(grid):
    gridcopy = copy.deepcopy(grid)

    for i in range(3):
        grid[0][i+3] = gridcopy[5-(i%3)][8]
        grid[i+3][0] = gridcopy[0][5-(i%3)]
        grid[8][i+3] = gridcopy[5-(i%3)][0]
        grid[i+3][8] = gridcopy[8][5-(i%3)]
        for j in range(3):
            grid[i+9][j+3] = gridcopy[11-(j%3)][i+3]

    return grid

def DP(grid):
    return D(D(D(grid)))

print_grid(B(create_grid()))