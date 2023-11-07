import time

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    start_time = time.time()

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    end_time = time.time()
    total_time = end_time - start_time

    return dp[n][capacity], total_time

def main():
    weights = list(map(int, input("Enter the weights of items (separated by space): ").split()))
    values = list(map(int, input("Enter the values of items (separated by space): ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    max_value, total_time = knapsack_dynamic_programming(weights, values, capacity)

    print("Maximum value in the knapsack:", max_value)
    print("Total time taken:", total_time, "seconds")

if __name__ == "__main__":
    main()

