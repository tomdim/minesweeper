import random

from .lists import LEVELS


def get_level(level):
    if level in LEVELS:
        return LEVELS.get(level)

    return {'error': 'Invalid level'}


def create_game(m, n, b):
    """
        Create a m x n minesweeper game where b is the number of bombs.
        Create a m x n neighboring bomb counts.
        :param m: integer
        :param n: integer
        :param b: integer
        :return: two 2D arrays (bombs, solution)
    """
    # Create bombs as a m+2 * n+2 array.
    bombs = [[False for x in range(m+2)] for y in range(n+2)]

    # bombs is [1..m][1..n]; the border is used to handle boundary cases.
    for r in range(1, m+1):
        for c in range(1, n+1):
            bombs[r][c] = (random.random() < 0.5)

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
