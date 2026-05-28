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

print("Hello")