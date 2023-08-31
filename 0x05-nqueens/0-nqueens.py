#!/usr/bin/python3
""" N Queens Interview Question """
import sys


try:
    size = int(sys.argv[1])
except IndexError:
    print("Usage: nqueens N")
    sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)
else:
    if size and size < 4:
        print("N must be at least 4")
        sys.exit(1)


solutions = []
positions = None


def can_attacc(p1, p2):
    """ Confirms if two queens are attacking each other """
    if (p1[0] == p2[0]) or (p1[1] == p2[1]):
        return True
    return abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])


def group_check(group):
    """ Check if a group is in solutions """
    global solutions
    for sol in solutions:
        i = 0
        for pos in sol:
            for grp_pos in group:
                if pos[0] == grp_pos[0] and pos[1] == grp_pos[1]:
                    i += 1
        if i == size:
            return True
    return False


def build(row, group):
    """ Builds a solution """
    global solutions
    global size
    if row == size:
        tmp0 = group.copy()
        if not group_check(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(size):
            a = (row * size) + col
            matches = zip(list([positions[a]]) * len(group), group)
            used_positions = map(lambda x: can_attacc(x[0], x[1]), matches)
            group.append(positions[a].copy())
            if not any(used_positions):
                build(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
        Gets the solutions for the specified chessboard size.
    """
    global positions, size
    positions = list(map(lambda x: [x // size, x % size], range(size ** 2)))
    a = 0
    group = []
    build(a, group)


get_solutions()
for sol in solutions:
    print(sol)
