import time

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))

start_time = time.time()
fibonacci_sequence = fibonacci_recursive(n)
end_time = time.time()

print("Fibonacci sequence (recursive):", fibonacci_sequence)
print("Total time taken (recursive):", end_time - start_time, "seconds")

