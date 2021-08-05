"""
An example of how to solve a Sudoku puzzle using Python.
"""
grid_string = ("003020600"
               "900305001"
               "001806400"
               "008102900"
               "700000008"
               "006708200"
               "002609500"
               "800203009"
               "005010300")

grid = [int(x) for x in grid_string]


def print_grid(g):
    """Print a grid"""
    for i in range(9):
        row = " ".join([f"{g[9 * i + j]}"for j in range(9)])
        print(row)
    print()


def valid(k, g):
    """Yield a number n, that can be inserted at index k, in grid g."""
    row = 9 * (k // 9)
    col = k % 9
    sqr = 27 * (k // 27) + 3 * (col // 3)

    for n in range(1, 10):
        if (n in g[row:row+9] or
            n in g[col::9] or
                n in g[sqr:sqr+3] + g[sqr+9:sqr+12] + g[sqr+18:sqr+21]):
            continue
        yield n


def solve(grid):
    """Solve a grid"""
    if not 0 in grid:
        return True
        
    k = grid.index(0)
    for n in valid(k, grid):
        grid[k] = n
        if solve(grid):
            return True

    grid[k] = 0
    return False


print_grid(grid)
solve(grid)
print_grid(grid)
