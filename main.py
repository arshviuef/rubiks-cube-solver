# Create 9x12 grid (each element initialised with empty string)
grid = [[""]*9 for _ in range(12)]

# Fill in values for grid (optimise later)
for i in range(len(grid)):
   for j in range(len(grid[i])):
        if j >= 3 and j <= 5:
            if i >= 0 and i <= 2:
                grid[i][j] = "w"
            elif i >= 3 and i <= 5:
                grid[i][j] = "b"
            elif i >= 6 and i <= 8:
                grid[i][j] = "y"
            else:
                grid[i][j] = "g"
        elif j >= 0 and j <= 2:
            if i >= 3 and i <= 5:
                grid[i][j] = "r"
        elif j >= 6 and j <= 8:
            if i >= 3 and i <= 5:
                grid[i][j] = "o"

# Print grid
for i in grid:
    print(i)


print("\n")


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