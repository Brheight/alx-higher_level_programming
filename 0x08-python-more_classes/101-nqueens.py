#!/usr/bin/python3
"""N-Queens Problem Solver"""

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen in the given cell.

    Args:
        board (list of list): The N x N chessboard.
        row (int): The current row.
        col (int): The current column.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_nqueens(board, col):
    """
    Recursive function to solve the N-Queens problem.

    Args:
        board (list of list): The N x N chessboard.
        col (int): The current column.

    Returns:
        list of list: A list of solutions, where each solution is a list of (row, column) coordinates for queens.
    """
    if col == len(board):
        solution = []
        for row in board:
            for i, val in enumerate(row):
                if val == 1:
                    solution.append([i, row.index(val)])
        return [solution]

    solutions = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            result = solve_nqueens(board, col + 1)
            if result:
                solutions.extend(result)
            board[i][col] = 0

    return solutions

def print_solutions(solutions):
    """
    Print the N-Queens solutions.

    Args:
        solutions (list of list): List of solutions, where each solution is a list of (row, column) coordinates for queens.
    """
    for solution in solutions:
        print(solution)

def main():
    """
    Main function to parse command-line arguments and solve the N-Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = solve_nqueens(board, 0)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
