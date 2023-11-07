def is_safe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    if col == n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_n_queens_solution(solution):
    for i, sol in enumerate(solution):
        print(f"Solution {i + 1}:")
        for row in sol:
            print(' '.join(['Q' if x == 1 else '.' for x in row]))
        print()

try:
    n = int(input("Enter the size of the N-Queens board: "))
    solutions = solve_n_queens(n)
    
    if solutions:
        print(f"Total {len(solutions)} distinct solutions found.")
        print_n_queens_solution(solutions)
    else:
        print("No solutions found for this board size.")
except ValueError:
    print("Please enter a valid integer for the board size.")
