import time

def fibonacci_non_recursive(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))

start_time = time.time()
fibonacci_sequence = fibonacci_non_recursive(n)
end_time = time.time()

print("Fibonacci sequence (non-recursive):", fibonacci_sequence)
print("Total time taken (non-recursive):", end_time - start_time, "seconds")

