import time

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row >= n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1  # First queen placed
    
    solutions = []
    
    start_time = time.time()
    solve_n_queens_util(board, 1, n, solutions)
    end_time = time.time()

    total_time = end_time - start_time
    return solutions, total_time

def main():
    n = int(input("Enter the number of queens: "))
    solutions, total_time = solve_n_queens(n)
    
    print(f"Total solutions for {n}-Queens problem: {len(solutions)}")
    print("Solutions:")
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(" ".join("Q" if col == 1 else "." for col in row))
        print()

    print("Total time taken:", total_time, "seconds")

if __name__ == "__main__":
    main()

