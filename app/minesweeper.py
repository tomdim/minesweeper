import random


def create_game(m, n, p):
    """
        Create a m x n minesweeper game where each cell is a bomb with
        probability p. Write the m x n game and the neighboring bomb counts
        to standard output.
        :param m: integer
        :param n: integer
        :param p: float
        :return: two arrays (bombs, solution)
    """
    # Create bombs as a m+2 * n+2 array.
    bombs = [[False for x in range(m+2)] for y in range(n+2)]

    # bombs is [1..m][1..n]; the border is used to handle boundary cases.
    for r in range(1, m+1):
        for c in range(1, n+1):
            bombs[r][c] = (random.random() < p)

    # Create solution as a m+2 x n+2 array.
    solution = [[0 for x in range(m+2)] for y in range(n+2)]

    # solution[i][j] is the number of bombs adjacent to cell (i, j).
    for r in range(1, m+1):
        for c in range(1, n+1):
            # (rr, cc) indexes neighboring cells.
            for rr in range(r-1, r+2):
                for cc in range(c-1, c+2):
                    if bombs[rr][cc]:
                        solution[r][c] += 1

    return bombs, solution
