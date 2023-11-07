def fibonacci_of(n):
  if n in {0, 1}:
        return n
  return fibonacci_of(n - 1) + fibonacci_of(n - 2)
[fibonacci_of(n) for n in range(15)]

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
import time
start=time.time()
nterms=9
for i in range(nterms):
       print(Fibonacci(i),end=" ")
print()
end=time.time()
total=end-start
print("total time is:",total,"ms")


