print("\n")

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

for row in grid:
    print(row)

def R(grid):
    col = [grid[i][5] for i in range(12)]
    for i in range(12): 
        grid[i][5] = col[(i+3) % 12]

    #rotate right side
    grid[3][6] = grid[3][8]
    grid[3][7] = grid[4][8]
    grid[3][8] = grid[5][8]

    grid[3][8] = grid[5][8]
    grid[4][8] = grid[5][7]
    grid[5][8] = grid[5][6]

    grid[5][8] = grid[5][6]
    grid[5][7] = grid[4][6]
    grid[5][6] = grid[3][6]

    grid[5][6] = grid[3][6]
    grid[4][6] = grid[3][7]
    grid[3][6] = grid[3][8]

    return grid

def RP(grid):
    grid = R(R(R(grid)))
    return grid

print("\n new grid")
grid = R(grid)
for row in grid:
    print(row)

print("\n R used 4 times")

grid = (R(R(R(grid))))

for row in (grid):
    print(row)

print("\n Right prime")

grid = RP(grid)
for row in grid:
    print(row)