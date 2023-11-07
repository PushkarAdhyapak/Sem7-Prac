class NQBacktracking:
    def __init__(self, x_, y_):
        self.ld = [0] * 30
        self.rd = [0] * 30
        self.cl = [0] * 30
        self.x = x_ - 1  # Adjust user input to match array indices starting from 0
        self.y = y_ - 1  # Adjust user input to match array indices starting from 0

    def printSolution(self, board):
        print(
            "N Queen Backtracking Solution:\nGiven initial position of 1st queen at row:",
            self.x + 1,  # Adjusted to show user's perspective (adding 1)
            "column:",
            self.y + 1,  # Adjusted to show user's perspective (adding 1)
            "\n",
        )
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col):
        if col >= N:
            return True

        if col == self.y:
            return self.solveNQUtil(board, col + 1)

        for i in range(N):
            if i == self.x:
                continue

            if (self.ld[i - col + N - 1] != 1 and self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self):
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1

        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True


if __name__ == "__main__":
    N = int(input("Enter the size of the board (N): "))
    x = int(input("Enter the row number for the initial position of the first queen: "))
    y = int(input("Enter the column number for the initial position of the first queen: "))

    NQBt = NQBacktracking(x, y)
    NQBt.solveNQ()

"""
The **N-Queens problem** is a classic combinatorial problem involving placing N queens on an NxN chessboard in a manner that no two queens can attack each other. The challenge is to determine all the distinct configurations of placing the queens.

### Backtracking

**Backtracking** is an algorithmic technique used for finding solutions to optimization problems, such as the N-Queens problem. It operates incrementally by constructing partial candidates for the solutions and abandoning a candidate as soon as it determines that the candidate cannot be a valid solution.

### Solving the N-Queens Problem using Backtracking

1. **Initial Placement of the First Queen:** The problem specifies the initial placement of the first queen. The rest of the queens will be placed using the backtracking algorithm.
  
2. **Placing Remaining Queens:** Using backtracking, you iteratively try placing the remaining queens in valid positions on the chessboard.
   
   - Start by placing the next queen in a column that hasn't been covered yet.
   - Check if placing the queen in the current position conflicts with the existing queens.
   - If a conflict is found, backtrack to the previous queen and explore a different position.
   - If a safe spot is found, place the queen there and proceed to place the next queen.
   - Continue this process recursively, ensuring each queen's placement is non-conflicting.

3. **Stopping Conditions:** The backtracking algorithm stops when all queens have been successfully placed on the board without attacking each other, or when all possible combinations have been explored.

4. **Generating Final N-Queens Matrix:** Upon successful placement of all queens, a valid solution has been found. The final result will be a valid N-Queens matrix demonstrating the arrangement of queens on the chessboard.

### Conclusion

Backtracking is a systematic way to find all possible solutions to the N-Queens problem. The algorithm explores different configurations methodically, ensuring each arrangement of queens doesn’t threaten each other. It continues until all valid combinations have been checked or the complete valid placement of queens is achieved. The final matrix represents the successful solution of the N-Queens problem.
"""
