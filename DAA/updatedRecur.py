# Recursive Fibonacci function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        # Recursively calculate Fibonacci numbers
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-Recursive Fibonacci function
def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)  # Print the first Fibonacci number
    if n > 1:
        print(second)  # Print the second Fibonacci number
    for _ in range(2, n):
        # Calculate the next Fibonacci number iteratively
        third = first + second
        first = second
        second = third
        print(third)

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers you want: "))
    for i in range(n):
        # Print Fibonacci numbers using the recursive function
        print(recursive_fibonacci(i))  # Recursive Fibonacci has exponential time and O(n) space complexity
    
    # Print Fibonacci numbers using the non-recursive function
    non_recursive_fibonacci(n)  # Non-recursive Fibonacci has linear (O(n)) time and constant (O(1)) space complexity


# Let's analyze the time and space complexity of the provided recursive and non-recursive Fibonacci implementations.

# **Recursive Fibonacci (`recursive_fibonacci` function):**

# Time Complexity:
# - The time complexity of the recursive Fibonacci function is exponential, specifically O(2^n). This is because it recalculates Fibonacci numbers for smaller values many times, leading to a large number of redundant calculations. For each call to `recursive_fibonacci`, it makes two recursive calls (for `n-1` and `n-2`).

# Space Complexity:
# - The space complexity of the recursive Fibonacci function is O(n) due to the recursion stack. In the worst case, there will be up to `n` function calls on the stack, and each call consumes space for its arguments and local variables.

# **Non-Recursive Fibonacci (`non_recursive_fibonacci` function):**

# Time Complexity:
# - The time complexity of the non-recursive Fibonacci function is O(n). It uses a simple loop to calculate and print the first `n` Fibonacci numbers. Each iteration of the loop computes the next Fibonacci number in constant time.

# Space Complexity:
# - The space complexity is O(1) because it uses a constant amount of extra space regardless of the input `n`. It only stores a few variables (e.g., `first`, `second`, `third`) that do not depend on `n`.

# In summary, the non-recursive approach is more efficient in terms of both time and space complexity, especially for large values of `n`, compared to the recursive approach, which has exponential time complexity and higher space usage due to the call stack.
# # 
