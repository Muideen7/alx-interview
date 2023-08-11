#!/usr/bin/python3
"""N-Queens problem solved with backtracking."""

import sys

def is_safe(board, row, col, N):
    '''Check if it's safe to place a queen in the given position.'''
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def nqueens_helper(board, row, N, solutions):
    '''Recursively find all solutions for N-Queens problem.'''
    if row == N:
        solution = [[r, c] for r in range(N) for c in range(N) if board[r][c] == 1]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            nqueens_helper(board, row + 1, N, solutions)
            board[row][col] = 0

def nqueens(N):
    '''Find and print all solutions for N-Queens problem.'''
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    nqueens_helper(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    nqueens(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

