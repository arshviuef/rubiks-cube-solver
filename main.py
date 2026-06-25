import copy
import random
import turtle


def create_grid():
    # Create 9x12 grid (each element initialised with empty string)
    grid = [[""] * 9 for _ in range(12)]

    faces = [
        ["g", 3, 5, 0, 2],
        ["w", 3, 5, 3, 5],
        ["b", 3, 5, 6, 8],
        ["y", 3, 5, 9, 11],
        ["r", 0, 2, 3, 5],
        ["o", 6, 8, 3, 5],
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
    gridcopy = copy.deepcopy(grid)

    col = [grid[i][5] for i in range(12)]
    for i in range(12):
        grid[i][5] = col[(i + 3) % 12]

    for i in range(3):
        for j in range(3):
            grid[i + 3][j + 6] = gridcopy[5 - (j % 6)][(i % 3) + 6]

    return grid


def RP(grid):
    return R(R(R(grid)))


def L(grid):
    gridcopy = copy.deepcopy(grid)

    col = [grid[i][3] for i in range(12)]
    for i in range(12):
        grid[i][3] = col[(i - 3) % 12]

    for i in range(3):
        for j in range(3):
            grid[i + 3][j] = gridcopy[5 - (j % 3)][i]

    return grid


def LP(grid):
    return L(L(L(grid)))


def D(grid):
    gridcopy = copy.deepcopy(grid)

    row = [grid[5][i] for i in range(9)]
    for i in range(9):
        grid[5][i] = row[(i - 3) % 9]

    for i in range(3):
        grid[5][i] = gridcopy[9][5 - i]
        grid[9][i + 3] = gridcopy[5][8 - i]
        for j in range(3):
            grid[i + 6][j + 3] = gridcopy[8 - (j % 3)][i + 3]

    return grid


def DP(grid):
    return D(D(D(grid)))


def U(grid):
    gridcopy = copy.deepcopy(grid)

    row = [grid[3][i] for i in range(9)]
    for i in range(9):
        grid[3][i] = row[(i + 3) % 9]

    for i in range(3):
        grid[3][i + 6] = gridcopy[11][5 - i]
        grid[11][i + 3] = gridcopy[3][2 - i]
        for j in range(3):
            grid[i][j + 3] = gridcopy[2 - (j % 3)][i + 3]

    return grid


def UP(grid):
    return U(U(U(grid)))


def F(grid):
    gridcopy = copy.deepcopy(grid)

    for i in range(3):
        grid[2][i + 3] = gridcopy[5 - i][2]
        grid[i + 3][2] = gridcopy[6][i + 3]
        grid[6][i + 3] = gridcopy[5 - i][6]
        grid[i + 3][6] = gridcopy[2][i + 3]
        for j in range(3):
            grid[i + 3][j + 3] = gridcopy[5 - (j % 3)][i + 3]

    return grid


def FP(grid):
    return F(F(F(grid)))


def B(grid):
    gridcopy = copy.deepcopy(grid)

    for i in range(3):
        grid[0][i + 3] = gridcopy[i + 3][8]
        grid[i + 3][0] = gridcopy[0][5 - (i % 3)]
        grid[8][i + 3] = gridcopy[i + 3][0]
        grid[i + 3][8] = gridcopy[8][5 - (i % 3)]
        for j in range(3):
            grid[i + 9][j + 3] = gridcopy[11 - (j % 3)][i + 3]

    return grid


def BP(grid):
    return B(B(B(grid)))


def randomise(grid):
    moves = [R, RP, L, LP, F, FP, B, BP, U, UP, D, DP]
    move_names = ["R", "RP", "L", "LP", "F", "FP", "B", "BP", "U", "UP", "D", "DP"]

    for _ in range(10):
        i = random.randint(0, len(moves) - 1)
        print("Move: " + move_names[i])
        grid = moves[i](grid)

    return grid


def draw_grid(grid):
    CELL = 50
    COLORS = {
        "w": "white",
        "b": "blue",
        "y": "yellow",
        "g": "green",
        "r": "red",
        "o": "orange",
        "": "lightgray",
    }

    # creating a turtle object called t that will do the drawing
    screen = turtle.Screen()
    screen.title("Rubik's Cube Net")
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(0, 0)

    # Grid is 9 cols x 12 rows, centre it on screen
    start_x = -(9 * CELL) / 2  # the negaive value shifts it to the left
    start_y = (12 * CELL) / 2

    for row in range(12):
        for col in range(9):
            color = COLORS[grid[row][col]]
            x = start_x + col * CELL
            y = start_y - row * CELL

            t.penup()
            t.goto(x, y)
            t.pendown()
            t.fillcolor(color)
            t.begin_fill()
            for _ in range(4):
                t.forward(CELL)
                t.right(90)
            t.end_fill()

    turtle.update()
    turtle.done()


if __name__ == "__main__":
    grid = create_grid()
    grid = randomise(grid)
    print_grid(grid)

    count = {"w": 0, "r": 0, "g": 0, "o": 0, "b": 0, "y": 0}
    for row in grid:
        for item in row:
            if item != "":
                count[item] += 1

    for key, value in count.items():
        print(f"{key}: {value}")
    draw_grid(grid)
